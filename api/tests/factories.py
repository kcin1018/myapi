import factory
from django.contrib.auth.models import User
#from .models import *

class UserFactory(factory.django.DjangoModelFactory):
    username = factory.Faker('user_name')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = factory.Faker('company_email')

    class Meta:
        model = User
