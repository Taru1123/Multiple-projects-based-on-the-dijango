from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def view1(request1):
    s1="this is 1st Response in myapp1"
    return HttpResponse(s1)
