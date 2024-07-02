from django.shortcuts import render
from .models import employee
# Create your views here.
def my_view(request):
    a=employee.objects.all()

    myName="tarun"
    favPlayer="dhoni"
    favAnimal="lion"
    favSubject="python"
    d={"name":myName,"player":favPlayer,"animal":favAnimal,"language":favSubject}
    k={'m':a}
    return render(request,"myapp/1.html",k)
