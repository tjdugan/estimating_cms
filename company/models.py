from django.db import models

# Create your models here.
class Company(models.Model):
    company_name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    website = models.URLField(max_length=150, null=True)
    phone = models.CharField(max_length=20)
    fax = models.CharField(max_length=20, null=True)
    
    def __str__(self):
        return self.company_name

class Employee(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    mobile = models.CharField(max_length=20, null=True)
    officeextension = models.CharField(max_length=20, null=True)
    email = models.EmailField(max_length=255)
    roll = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.firstname}  {self.lastname}"