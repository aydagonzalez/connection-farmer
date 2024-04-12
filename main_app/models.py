from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date


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
    full_name = models.CharField(blank = True, max_length=50)
    picture_url = models.TextField(blank = True)
    linkedin_url = models.CharField(max_length=200, blank = True)
    industry = models.CharField(max_length=200, blank = True)
    number_connections = models.IntegerField(default =0, blank = True)
    total_time_spent = models.IntegerField(default =0, blank = True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)

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
    confidence_bar = models.IntegerField("Confidence Rating (0-10):", default=10)
    desirability_bar = models.IntegerField("Desirability Rating (0-10):", default=10)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'job_id': self.id})

class Event(models.Model):
    date = models.DateField()
    type_of_event = models.CharField(
        max_length=200,
        choices = EVENTS,
        default= EVENTS[0][0],)
    time_spent = models.IntegerField()
    comment = models.TextField()
    job = models.ForeignKey(Job, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('job_detail', kwargs={'job_id': self.job.id})