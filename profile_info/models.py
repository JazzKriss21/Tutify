from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.conf import settings
from django.db.models.signals import post_delete
from django.dispatch import receiver

def upload_location(instance, filename):
	file_path = 'blog/{author_id}/{title}-{filename}'.format(
				author_id=str(instance.author.id),title=str(instance.title), filename=filename)
	return file_path


class TutorProfile(models.Model):
	account					= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	location  				= models.CharField(max_length = 50, blank=False)
	subjects				= models.TextField(blank=False)
	qualification			= models.CharField(max_length = 256, blank=False)
	bio 					= models.TextField(max_length=5000, null=False, blank=False)
	gender 					= models.CharField(max_length=10, null=False, blank=False)
	image		 			= models.ImageField(upload_to=upload_location, null=True, blank=True)
	hourly_rate 			= models.IntegerField()
	slug 					= models.SlugField(blank=True, unique=True)

	def __str__(self):
		return self.title

@receiver(post_delete, sender=TutorProfile)
def submission_delete(sender, instance, **kwargs):
    instance.image.delete(False) 

def pre_save_tutor_profile_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = slugify(instance.account.username)

pre_save.connect(pre_save_tutor_profile_receiver, sender=TutorProfile)


