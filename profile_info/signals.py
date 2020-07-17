from django.db.models.signals import post_save #this is a signal that gets fired when an object is saved
from django.contrib.auth.models import User #user will be sending the signal
from django.dispatch import receiver # a receiver is a function that gets this signal and then performs tasks
from profile_info.models import Profile
from django.conf import settings

@receiver(post_save,sender=settings.AUTH_USER_MODEL) # when a user is saved then send post-save signal and this signal is received by receiever(create_profile)
def create_profile(sender,instance,created,**kwargs):  #we want a user profile that has to be created for every user
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def save_profile(sender,instance, **kwargs):
    instance.profile.save()
