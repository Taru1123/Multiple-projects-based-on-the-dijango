from django.contrib import admin
from myapp.models import employee
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    l=['phnu','name','eid','salary','company']
admin.site.register(employee,StudentAdmin)