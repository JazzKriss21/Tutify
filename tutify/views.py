from django.shortcuts import render
from friendship.models import Friend, Follow, Block, FriendshipRequest
from accounts.models import Account
from django.http import HttpResponseRedirect
from profile_info.views import profile_view
from profile_info.models import Profile, TutorProfile


def homepage_view(request):
    return render(request, 'tutify/index.html')

def faq_view(request):
	return render(request, 'tutify/faq.html')

def contact_view(request):
	return render(request, 'tutify/contact.html')

def follow_view(request, reciever):
	user2=Account.objects.get(username=reciever)
	Follow.objects.add_follower(request.user, user2)

	users=Profile.objects.all()
	tutors=TutorProfile.objects.all()
	current_user=request.user
	context={
		'user':user2,
		'users':users,
		'tutors':tutors,
		'current_user':current_user
	}
	return render(request, 'profile_info/profile.html',context=context)

def friend_request_view(request, reciever):
	user2=Account.objects.get(username = reciever)
	Friend.objects.add_friend(request.user, user2)
	users=Profile.objects.all()
	tutors=TutorProfile.objects.all()
	current_user=request.user
	context={
		'user':user2,
		'users':users,
		'tutors':tutors,
		'current_user':current_user
	}
	return render(request, 'profile_info/profile.html',context=context)