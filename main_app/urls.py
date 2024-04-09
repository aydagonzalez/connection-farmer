from django.urls import path
from . import views



urlpatterns = [
  path('', views.home, name='home'),
  path('accounts/signup/', views.signup, name='signup'),
  path('profiles/', views.profiles_index, name='index'),
  path('profiles/<int:profile_id>/', views.profiles_detail, name='detail'),
  path('jobs/<int:job_id>', views.jobs_detail, name='job_detail'),
  path('accounts/profile/', views.signup, name='signup'),

]