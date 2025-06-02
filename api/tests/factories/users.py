import factory
from factory.django import DjangoModelFactory
from django.contrib.auth.models import Group

from api.models import User
from api.tests.common import DEFAULT_PASSWORD


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker('user_name')
    password = factory.Faker('password')
    
    @factory.post_generation
    def password(self, create, extracted, **kwargs):
        if not create:
            return
        
        if extracted:
            self.set_password(extracted)
        else:
            self.set_password(DEFAULT_PASSWORD)
        
        self.save()
        
    @factory.post_generation
    def groups(self, create, extracted, **kwargs):
        if not create:
            return
        
        if extracted:
            group = Group.objects.get(name=extracted)
            self.groups.add(group)
                

class GroupFactory(DjangoModelFactory):
    class Meta:
        model = Group