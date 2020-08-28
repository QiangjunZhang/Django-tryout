from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        new = Profile.objects.create(user=instance)
        new.save()


# @receiver(post_save, sender=User)
# def create_profile(sender, instance, **kwargs):
#     instance.profile.save()
