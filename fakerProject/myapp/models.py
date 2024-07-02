from django.db import models

# Create your models here.
class Students(models.Models):
	name=models.CharacterField(max_Length=30)
	roll=models.IntegerField()
	marks=models.CharacterField()
	Dob=models.DataField()
