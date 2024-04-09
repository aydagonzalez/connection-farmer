from django.urls import path
from . import views



urlpatterns = [
  path('', views.home, name='home'),
  path('accounts/signup/', views.signup, name='signup'),
  path('profiles/', views.profiles_index, name='index'),
  path('profiles/<int:profile_id>/', views.profiles_detail, name='detail'),
  path('jobs/<int:job_id>', views.jobs_detail, name='job_detail'),
  path('accounts/profile/', views.signup, name='signup'),
  path('jobs/<int:pk>/delete/', views.JobDelete.as_view(), name='jobs_delete'),
  path('profiles/<int:profile_id>/add_job/', views.add_job, name='add_job'),
  path('jobs/<int:pk>/update/', views.JobUpdate.as_view(), name='jobs_update'),
]