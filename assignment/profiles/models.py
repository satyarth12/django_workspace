from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

from user.models import CustomUser


class Team(models.Model):

    class NameTypes(models.TextChoices):
        DEVELOPMENT = 'DEVELOPMENT', _('Development')
        PRODUCT = 'PRODUCT', _('Product')
        DESIGN = 'DESIGN', _('Design')
        HUMAN_RESOURCE = 'HUMAN_RESOURCE', _('Human Resource')

    name = models.CharField(max_length=100, unique=True,
                            choices=NameTypes.choices)

    def __str__(self):
        return self.name


class Profile(models.Model):

    user = models.OneToOneField(to=CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=350, help_text=_(
        "User's Full Name"), null=True)
    designation = models.CharField(
        max_length=350, help_text=_("User's Designation"), null=True)
    profile_picture = models.ImageField(upload_to="media/")
    team = models.ManyToManyField(Team, null=True, blank=True)

    def __str__(self):
        return self.user.email
