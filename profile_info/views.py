from django.shortcuts import render,redirect
from .models import Profile
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
	current_user=request.user
	if request.method == 'POST':
	# # 	u_form=UserUpdateForm(request.POST,instance=request.user)
		p_form=ProfileUpdateForm(request.POST,request.FILES,instance=user)
		if  p_form.is_valid():
			# u_form.save()
			p_form.save()

	else:
	# # 	u_form=UserUpdateForm(instance=request.user)
		p_form=ProfileUpdateForm(instance=user)
	context={
		# 'u_form':u_form,
		'p_form':p_form,
		'users':users,
		'current_user':current_user
	}
	return render(request, 'profile_info/profile.html',context=context)

