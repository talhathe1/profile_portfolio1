from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Applicant)
admin.site.register(Project)
admin.site.register(Education)
admin.site.register(Skill)
admin.site.register(Job)