from django.db import models

# Create your models here.
class Contractor(models.Model):
    company_name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    website = models.URLField(max_length=150, null=True)
    phone = models.CharField(max_length=20)
    fax = models.CharField(max_length=20, null=True)
    
    def __str__(self):
        return self.company_name

class ProjectManager(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    mobile = models.CharField(max_length=20)
    officenumber = models.CharField(max_length=20)
    email = models.EmailField(max_length=255)
    company = models.ForeignKey('Contractor', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.firstname}  {self.lastname}"

class Architect(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    phone = models.CharField(max_length=20, null=True)
    website = models.URLField(max_length=150, null=True)

    def __str__(self):
        return self.name

class Supplier(models.Model):
    company_name = models.CharField(max_length=150)
    address = models.CharField(max_length=250)
    phone = models.CharField(max_length=20)
    website = models.URLField(max_length=150)

    def __str__(self):
        return self.company_name

class Salesman(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=20, null=True)
    office_number = models.CharField(max_length=20, null=True)
    email = models.EmailField(max_length=150, null=True)
    company = models.ForeignKey('Supplier', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Manufacturer(models.Model):
    company_name = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    phone = models.CharField(max_length=20)
    website = models.URLField(max_length=100)

    def __str__(self):
        return self.company_name

class ProductRep(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    mobile = models.CharField(max_length=20, null=True)
    office_number = models.CharField(max_length=20, null=True)
    email = models.EmailField(max_length=150, null=True)
    company = models.ForeignKey('Manufacturer', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"