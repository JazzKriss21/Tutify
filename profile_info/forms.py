from django import forms
from .models import TutorProfile 


class TutorProfileForm(forms.ModelForm):
	class Meta:
		model = TutorProfile
		fields = ['location', 'subject', 'qualification', 'gender', 'bio', 'hourly_rate']


class UpdateTutorProfileForm(forms.ModelForm):

	class Meta:
		model = TutorProfile
		fields = ['location', 'subject', 'qualification', 'gender', 'bio', 'hourly_rate']

	def save(self, commit=True):
		tutor_profile = self.instance
		tutor_profile.location = self.cleaned_data['location']
		tutor_profile.subject = self.cleaned_data['subject']
		tutor_profile.qualification = self.cleaned_data['qualification']
		tutor_profile.gender = self.cleaned_data['gender']
		tutor_profile.bio = self.cleaned_data['bio']
		tutor_profile.hourly_rate = self.cleaned_data['hourly_rate']

		if self.cleaned_data['image']:
			tutor_profile.image = self.cleaned_data['image']

		if commit:
			tutor_profile.save()
		return tutor_profile

