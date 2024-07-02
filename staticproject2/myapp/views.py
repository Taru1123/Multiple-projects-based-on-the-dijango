from django.shortcuts import render

# Create your views here.
def myview(request):
	name="taru"
	favPlayer="dhoni"
	favAnimal="lion"
	favSubject="python"
	d={"name":name,"player":favPlayer,"animal":favAnimal,"subject":favSubject}
	return render(request,'myapp/1.html',d)