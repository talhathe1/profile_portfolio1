from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import *

def members(request):

  mymembers = Applicant.objects.all()
  studys = Education.objects.all() 
  experience = Job.objects.all() 
  pro = Project.objects.all()

  return render(request, "home.html", {"mymembers": mymembers, "studys": studys, "experience": experience, "pro": pro}) 


def projects(request):

  pro = Project.objects.all()
 
  return render(request, "projects.html", {"pro": pro})  

def project_details(request):

  return render(request, "project-details.html")

def specialization(request):

  return render(request, "specialization.html")
