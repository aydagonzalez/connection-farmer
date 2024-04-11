from django.urls import path
from . import views



urlpatterns = [
  path('', views.home, name='home'),
  path('accounts/signup/', views.signup, name='signup'),
  path('profiles/', views.profiles_index, name='index'),
  path('profiles/<int:profile_id>/', views.profiles_detail, name='detail'),
  path('profileform/', views.ProfileCreate.as_view(), name='profileform'),
  path('profiles/<int:pk>/update/', views.ProfileUpdate.as_view(), name='profile_update'),
  # path('createprofile/', views.profiles_create, name='create_profile'),
  path('jobs/<int:job_id>', views.jobs_detail, name='job_detail'),
  path('accounts/profile/', views.signup, name='signup'),
  path('jobs/<int:pk>/delete/', views.JobDelete.as_view(), name='jobs_delete'),
  path('profiles/<int:profile_id>/add_job/', views.add_job, name='add_job'),
  path('jobs/<int:pk>/update/', views.JobUpdate.as_view(), name='jobs_update'),
  path('jobs/<int:job_id>/add_event/', views.add_event, name='add_event'),
  path('events/<int:pk>/update/', views.EventUpdate.as_view(), name='events_update'),
  path('events/<int:pk>/delete/', views.EventDelete.as_view(), name='events_delete'),
]