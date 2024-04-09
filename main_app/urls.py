from django.urls import path
from . import views



urlpatterns = [
  path('', views.home, name='home'),
  path('accounts/signup/', views.signup, name='signup'),
  path('profiles/', views.profiles_index, name='index'),
  path('profiles/<int:profile_id>/', views.profiles_detail, name='detail'),
]