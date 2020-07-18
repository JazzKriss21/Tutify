from django.contrib import admin

# Register your models here.

from profile_info.models import TutorProfile
from .models import Profile

admin.site.register(Profile)
admin.site.register(TutorProfile)
