from django.db import models

class employee(models.Model):
    phnu=models.IntegerField()
    name=models.CharField(max_length=30)
    eid=models.FloatField()
    slary=models.IntegerField()
    company=models.CharField(max_length=50)

    def __str__(self):
        return self.name
