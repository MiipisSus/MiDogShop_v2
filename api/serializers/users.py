from rest_framework import serializers
from django.contrib.auth.models import Group

from api.models import User, CustomerAddressHome


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['user_permissions', 'groups',
                   'is_superuser', 'is_staff', 'is_active']
        read_only_fields = ['last_login',
                            'date_joined', 'groups', 'user_permissions']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        # encode password
        instance: User = super().create(validated_data)
        instance.set_password(instance.password)
        instance.save()
        customer_group = Group.objects.get(name='Customer')
        instance.groups.add(customer_group)
        return instance

    def update(self, instance, validated_data):
        # encode password
        instance: User = super().update(instance, validated_data)
        instance.set_password(instance.password)
        instance.save()
        return instance


class CustomerAddressHomeSerializer(serializers.ModelSerializer):
    customer_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='customer', write_only=True
    )
    customer = UserSerializer(read_only=True)
    
    class Meta:
        model = CustomerAddressHome
        fields = '__all__'
    
    def validate_customer_id(self, value):
        request = self.context.get('request')
        if not request.user.is_superuser:
            if value != request.user:
                raise serializers.ValidationError('You can only create your own address home.')
        
        return value