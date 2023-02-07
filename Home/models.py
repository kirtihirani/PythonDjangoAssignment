from django.db import models

# Create your models here.
class Employee(models.Model):
    empname = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    contact = models.CharField(max_length=12)
    manager = models.CharField(max_length=10,default='no')
    def __str__(self):
        return self.empname

class Department(models.Model):
    deptname = models.CharField( max_length=50)
    manager = models.OneToOneField(Employee, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.deptname