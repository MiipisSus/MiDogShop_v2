from rest_framework import serializers
from django.contrib.auth.models import Group

from api.models import User, CustomerAddressHome


class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    exclude = ['user_permissions', 'groups', 'is_superuser', 'is_staff', 'is_active']
    read_only_fields = ['last_login', 'date_joined', 'groups', 'user_permissions']
    extra_kwargs = {
      'password': {'write_only': True}
    }
  
  def validate(self, data):
        request_user = self.context['request'].user
        instance_user = self.instance

        if instance_user and request_user != instance_user and not request_user.is_staff:
            raise serializers.ValidationError({"detail": "你無權修改其他使用者的資料。"})
        
        return data
      
  def create(self, validated_data):
    # encode password
    user = User.objects.create_user(**validated_data)
    customer_group = Group.objects.get(name='Customer')
    user.groups.add(customer_group)
    return user
  

class CustomerAddressHomeSerializer(serializers.ModelSerializer):
  class Meta:
    model = CustomerAddressHome
    fields = '__all__'