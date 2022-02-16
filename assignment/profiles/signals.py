from django.db.models.signals import post_save
from django.dispatch import receiver

from user.models import CustomUser
from .models import Profile


@receiver(post_save, sender=CustomUser)
def create_profile(sender, instance, created, **kwargs):
    """creates a user's one-to-one profile object 
    """
    if created:
        Profile.objects.create(user=instance)
