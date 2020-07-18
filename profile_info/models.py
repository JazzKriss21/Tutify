from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.conf import settings
from django.db.models.signals import post_delete
from django.dispatch import receiver

#user profilepic
from django.contrib.auth.models import User

class Profile(models.Model):
	user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
	image=models.ImageField(default='default.jpg',upload_to='profile_pics')
	Date_of_Birth=models.DateField(blank=True,null=True)
	Bio=models.TextField(max_length=200,blank=True,null=True)
	City=models.TextField(max_length=200,null=True,blank=True)
	def __str__(self):
		return f'{self.user.username} Profile'


def upload_location(instance, filename):
	file_path = 'blog/{author_id}/{title}-{filename}'.format(
				author_id=str(instance.author.id),title=str(instance.title), filename=filename)
	return file_path


class TutorProfile(models.Model):
	key					= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	location  				= models.CharField(max_length = 50, blank=True,  null=True)
	subjects				= models.TextField(blank=True, null=True)
	qualification			= models.CharField(max_length = 256, blank=True, null=True)
	bio 					= models.TextField(max_length=5000, null=True, blank=True)
	gender 					= models.CharField(max_length=10, null=True, blank=True)
	image		 			= models.ImageField(upload_to='profile_pics', null=True, blank=True)
	hourly_rate 			= models.IntegerField()
	availabilty 			= models.CharField(max_length=50, blank=True, default='Both')
	proof 					= models.ImageField(upload_to='tutor_proof', null=True, blank=True)
	verfied					= models.BooleanField(null=True, blank=True, default=False)
	slug 					= models.SlugField(null=True, blank=True, unique=True)

	def __str__(self):
		return self.key.username

@receiver(post_delete, sender=TutorProfile)
def submission_delete(sender, instance, **kwargs):
    instance.image.delete(False)

def pre_save_tutor_profile_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = slugify(instance.key.username)

pre_save.connect(pre_save_tutor_profile_receiver, sender=TutorProfile)


