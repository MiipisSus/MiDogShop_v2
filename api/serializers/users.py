from rest_framework.serializers import ModelSerializer, ValidationError
from django.contrib.auth.models import Group

from api.models import User, CustomerAddressHome


class UserSerializer(ModelSerializer):
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


class CustomerAddressHomeSerializer(ModelSerializer):
    class Meta:
        model = CustomerAddressHome
        fields = '__all__'