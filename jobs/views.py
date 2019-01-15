from django.shortcuts import render

from .models import Job

def index(request):
	jobs = Job.objects
	return render(request, 'jobs/index.html', {'jobs': jobs, 'home_page':'active'})

def about(request):
	return render(request, 'jobs/about.html',{'about':'about','about_page':'active'})
