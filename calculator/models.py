from django.db import models
from user_profile.models import UserProfile

class Calculations(models.Model):
    id = models.IntegerField(primary_key=True)
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    entries = models.CharField(max_length=150)
