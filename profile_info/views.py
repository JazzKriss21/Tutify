from django.shortcuts import render,redirect
from .models import Profile, TutorProfile
from .forms import UserUpdateForm,ProfileUpdateForm,TutorProfileForm
from django.contrib.auth.decorators import login_required
from accounts.models import Account
from .forms import ProfileForm


def student_profile(request):
	# user=Account.objects.get(username=username)
	current_user=request.user
	if request.method=='POST':
		form=ProfileForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return redirect('home')
	else:
		form=ProfileForm()
	context={
		'form':form,
		'current_user':current_user,
	}
	return render(request,'profile_info/student.html',context=context)


def tutor_profile(request):
	# user=Account.objects.get(username=username)
	current_user=request.user
	if request.method=='POST':
		form=TutorProfileForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return redirect('home')
	else:
		form=TutorProfileForm()
	context={
		'form':form,
		'current_user':current_user,
	}
	return render(request,'profile_info/tutor_register.html',context=context)


@login_required
def profile_view(request,username):
	user=Account.objects.get(username=username)
	users=Profile.objects.all()
	tutors=TutorProfile.objects.all()
	current_user=request.user
	context={
		'user':user,
		'users':users,
		'tutors':tutors,
		'current_user':current_user
	}
	return render(request, 'profile_info/profile.html',context=context)

def update_profile(request,username):
	user=Account.objects.get(username=username)
	form=ProfileForm(instance=user)
	if request.method=='POST':
		form=ProfileForm(request.POST,instance=user)
		if form.is_valid():
			form.save()
			return redirect('home')
	context={
		'form':form,
		'user':user
	}
	return render(request,'profile_info/profile_update.html',context=context)


