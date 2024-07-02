import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fakerProject.settings')
django.setup()
from faker import Faker
from myapp.models import student
f=Faker()
def generate_data(n):
  for i in range(n):
    name=f.name()
    roll=f.random_int(min=1,max=100)
    marks=f.pyint(min_value=0,max_value=100)
    dob=f.date()
    email=f.email()
    s=student.objects.get_or_create(name=name,roll=roll,marks=marks,dob=dob,email=email)
generate_data(20)
