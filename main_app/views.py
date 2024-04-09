from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Profile, Job, Event
from .forms import JobForm

# Create your views here.
def home(request):
  return render(request, 'home.html')

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid signup. Please try again.'
  form = UserCreationForm()

  context = {
    'form': form,
    'error_message': error_message,
  }

  return render(request, 'registration/signup.html', context)

def profiles_index(request):
  profiles = Profile.objects.all()
  return render(request, 'profiles/index.html', {
    'profiles': profiles
  })


def profiles_detail(request, profile_id):
    profile = Profile.objects.get(id=profile_id)
    jobs = Job.objects.filter(profile =profile_id)
    job_form = JobForm()
    return render(request, 'profiles/detail.html', {
        'jobs': jobs,
        'job_form': job_form
    })

def jobs_detail(request, job_id):
  job = Job.objects.get(id=job_id)
  events = Event.objects.filter(job=job_id)
  return render(request, 'profiles/jobs/detail.html', {
    'events': events,
    'job': job
  })


class JobDelete(DeleteView):
  model = Job
  success_url = '/profiles'

def add_job(request, profile_id):
  form = JobForm(request.POST)
  if form.is_valid():
    new_job = form.save(commit=False)
    new_job.profile_id = profile_id
    new_job.save()
  return redirect('detail', profile_id=profile_id)
