from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

from user.models import CustomUser


class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    def save(self, *args, **kwargs):
        self.name = self.name.capitalize()
        super(Team, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Profile(models.Model):

    user = models.OneToOneField(to=CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=350, help_text=_("User's Full Name"))
    designation = models.CharField(
        max_length=350, help_text=_("User's Designation"))
    profile_picture = models.ImageField(upload_to="media/")
    team = models.ManyToManyField(Team)

    def __str__(self):
        return self.user.email
