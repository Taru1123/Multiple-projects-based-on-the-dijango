from django.shortcuts import render
from myapp.models import Student
from myapp.forms import StudentForm
# Create your views here.
def input_view(request):
	f=StudentForm()
	if request.method=="POST":
		f=StudentForm(request.POST)
		if f.is_valid():
			f.save(commit=True)
	return render(request,'myapp/1.html',{'form':f})