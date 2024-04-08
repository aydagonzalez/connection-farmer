from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

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