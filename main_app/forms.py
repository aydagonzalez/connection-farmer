from django.forms import ModelForm, Textarea, TextInput
from .models import Job, Event, Profile

class JobForm(ModelForm):
  class Meta:
    model = Job
    fields = ['position_applied_for', 'company_name', 'salary_range', 'status', 'type_of_resume', 'dates', 'confidence_bar', 'desirability_bar']
    
class EventForm(ModelForm):
  class Meta:
    model = Event
    fields = ['date', 'type_of_event', 'time_spent', 'comment']  
    widgets = {
      'comment': Textarea(attrs={'cols': 80, 'rows': 20})
    }

class ProfileForm(ModelForm):
  class Meta:
    model = Profile
    fields = ['full_name', 'picture_url', 'linkedin_url', 'industry', 'number_connections']
