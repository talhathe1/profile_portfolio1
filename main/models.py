from typing import Any
from django.db import models


# Create your models here.
class Applicant(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    image = models.ImageField(null = True, blank = True, upload_to='images/')
    description = models.TextField(null=True, blank=True)
    link = models.CharField(null=True, blank=True ,max_length=100)
    _id = models.AutoField(primary_key=True, editable=False)
    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=100)
    applicant = models.ForeignKey(Applicant, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(null = True, blank = True, upload_to='images/')
    description = models.TextField(null=True, blank=True)
    link = models.CharField(null=True, blank=True ,max_length=100)
    _id = models.AutoField(primary_key=True, editable=False)
    def __str__(self):
        return self.name
    
class Education(models.Model):
    degree = models.CharField(max_length=100)
    applicant = models.ForeignKey(Applicant, on_delete=models.SET_NULL, null=True)
    institue = models.CharField(null=True, blank=True ,max_length=100)
    started_at = models.DateField(null=True, blank=True)
    completed_at = models.DateField(null=True, blank=True)
    image = models.ImageField(null = True, blank = True, upload_to='images/')
    description = models.TextField(null=True, blank=True)
    link = models.CharField(null=True, blank=True ,max_length=100)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return self.degree
    
    
class Job(models.Model):
    name = models.CharField(max_length=100)
    applicant = models.ForeignKey(Applicant, on_delete=models.SET_NULL, null=True)
    company = models.CharField(null=True, blank=True ,max_length=100)
    started_at = models.DateField(null=True, blank=True)
    completed_at = models.DateField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    link = models.CharField(null=True, blank=True ,max_length=100)
    _id = models.AutoField(primary_key=True, editable=False)
    def __str__(self):
        return self.name
    
class Skill(models.Model):
    name = models.CharField(max_length=100)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    applicant = models.ForeignKey(Applicant, on_delete=models.SET_NULL, null=True)
    description = models.CharField(null=True, blank=True ,max_length=100)
    link = models.CharField(null=True, blank=True ,max_length=100)
    _id = models.AutoField(primary_key=True, editable=False)
    def __str__(self):
        return self.name
