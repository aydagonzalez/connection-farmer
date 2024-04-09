from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


APPLICATION_STATUS =(
    ('open', 'open'),
    ('closed','closed'),
    )

RESUME_TYPE = (
    ('targeted', 'targeted'),
    ('spam', 'spam')
)

EVENTS = (
    ('applied', 'applied'),
    ('interview', 'interview'),
    ('accepted', 'accepted'),
    ('rejected', 'rejected')
)

# Create your models here.
class Profile(models.Model):
    full_name = models.CharField(max_length=50)
    picture_url = models.TextField()
    linkedin_url = models.CharField(max_length=200)
    industry = models.CharField(max_length=200)
    number_connections = models.IntegerField()
    total_time_spent = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.full_name} ({self.id})'

    def get_absolute_url(self):
        return reverse('detail', kwargs={'profile_id': self.id})
    

class Job(models.Model):
    position_applied_for = models.CharField(max_length=50)
    company_name = models.CharField(max_length=50)
    salary_range = models.IntegerField()
    status = models.CharField(
        max_length=200,
        choices = APPLICATION_STATUS,
        default= APPLICATION_STATUS[0][0],)
    type_of_resume = models.CharField(
        max_length=200,
        choices = RESUME_TYPE,
        default= RESUME_TYPE[0][0],)
    dates = models.DateField()
    time_spent = models.IntegerField()
    confidence_bar = models.IntegerField()
    desirability_bar = models.IntegerField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

class Event(models.Model):
    date = models.DateField()
    type_of_event = models.CharField(
        max_length=200,
        choices = EVENTS,
        default= EVENTS[0][0],)
    time_spent = models.IntegerField()
    comment = models.TextField()
    job = models.ForeignKey(Job, on_delete=models.CASCADE)