from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Profile

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