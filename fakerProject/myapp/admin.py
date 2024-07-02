from django.contrib import admin
from myapp.models import student

# Register your models here.
class studentAdmin(admin.ModelAdmin):
    l=['name','roll','marks','Dob','email']
admin.site.register(student,studentAdmin)