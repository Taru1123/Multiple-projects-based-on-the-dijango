from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def view1(request):
    s="<h1> this is the 1st Response"
    return HttpResponse(s)
def view2(request):
    n1 = int(input("eneter the 1st number:"))
    n2 = int(input("enter the 2nd number:"))
    n3 = int(input("enter the 3red number"))
    n4 = n1+n2+n3
    return HttpResponse(str(n3))
 