from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def view1(request):
    s1='this is the first response'
    return HttpResponse(s1)

def view2(request):
    s2='this is the second response'
    return HttpResponse(s2)