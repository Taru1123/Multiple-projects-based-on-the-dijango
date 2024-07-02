from django.shortcuts import render

# Create your views here.
def templets_view(request):
    return render(request,'myapp/1.html')