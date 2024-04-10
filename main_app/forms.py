from django.forms import ModelForm
from .models import Job, Event, Profile

class JobForm(ModelForm):
  class Meta:
    model = Job
    fields = ['position_applied_for', 'company_name', 'salary_range', 'status', 'type_of_resume', 'dates', 'time_spent', 'confidence_bar', 'desirability_bar']
    
class EventForm(ModelForm):
  class Meta:
    model = Event
    fields = ['date', 'type_of_event', 'time_spent', 'comment']  

class ProfileForm(ModelForm):
  class Meta:
    model = Profile
    fields = ['full_name', 'picture_url', 'linkedin_url', 'industry', 'number_connections']
