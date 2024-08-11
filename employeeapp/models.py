from django.db import models

# Create your models here.

#create data bse models for EMployee 

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(null=False)
    age = models.IntegerField(null=False)
    gennder = models.CharField(max_length=10,null=False,default=20)
    phone_no =models.CharField(max_length=12,null=False,default="")
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)

class AddressDetails(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='address')
    house_no = models.CharField(max_length=100, null=False)
    street = models.CharField(max_length=100, null=False)
    city = models.CharField(max_length=100, null=False)
    state=models.CharField(max_length=100, null=False)
    country = models.CharField(max_length=100, null=False)


class workExperience(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='work_experience')
    company_name = models.CharField(max_length=100, null=False)
    designation = models.CharField(max_length=100, null=False)
    from_date = models.DateField(null=False)
    to_date = models.DateField(null=False)
    address=models.CharField(max_length=100, null=False)

class Qualification(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='qualification')
    qualification = models.CharField(max_length=100, null=False)
    pecentage = models.FloatField(null=False)
    year = models.IntegerField(null=False)  


class projects(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='projects')
    title = models.CharField(max_length=100, null=False)
    description = models.TextField(null=False)
