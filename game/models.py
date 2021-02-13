from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models
import datetime



class User(AbstractUser):
    pass



class Quarterback(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)  
    name = models.CharField(max_length=20, blank=True)
    score = models.FloatField(blank=True, null=True)

     
class Runningback(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)  
    name = models.CharField(max_length=20, blank=True)
    score = models.FloatField(blank=True, null=True)


class Widereceiver(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)  
    name = models.CharField(max_length=20, blank=True)
    score = models.FloatField(blank=True, null=True)


class Tightend(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)  
    name = models.CharField(max_length=20, blank=True) 
    score = models.FloatField(blank=True, null=True)

            
class Kicker(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)  
    name = models.CharField(max_length=20, blank=True) 
    score = models.FloatField(blank=True, null=True)


class Team(models.Model):
    team_name = models.CharField(max_length=255, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    quarter_back = models.ForeignKey(Quarterback, on_delete=models.CASCADE, null=True)
    running_back = models.ForeignKey(Runningback, on_delete=models.CASCADE, null=True)
    wide_receiver = models.ForeignKey(Widereceiver, on_delete=models.CASCADE, null=True)
    tight_end = models.ForeignKey(Tightend, on_delete=models.CASCADE, null=True)
    kicker = models.ForeignKey(Kicker, on_delete=models.CASCADE, null=True)
    teamscore = models.FloatField(blank=True, null=True)
