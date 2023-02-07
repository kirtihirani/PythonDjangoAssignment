from django.contrib import admin

from Home.models import Department, Employee

# Register your models here.
admin.site.register(Employee)
admin.site.register(Department)