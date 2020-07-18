from django.shortcuts import render
from .filters import TutorFilter
from profile_info.models import TutorProfile
# Create your views here.

def student_dashboard_view(request):
	tutor_list = TutorProfile.objects.all()
	filter = TutorFilter(request.GET, queryset=tutor_list)  # Ask
	tutor_list = filter.qs
	context={
		'tutor_list':tutor_list,
		'filter':filter
	}
	return render(request, 'dashboard/studentpage_afterlogin.html',context=context)

def tutor_dashboard_view(request):
	return render(request, 'dashboard/tutorpage_afterlogin.html')

def result_search_view(request):
	tutor_list = TutorProfile.objects.all()
	filter = TutorFilter(request.GET, queryset=tutor_list)  # Ask
	tutor_list = filter.qs
	context = {
		'tutor_list': tutor_list,
		'filter': filter
	}
	return render(request, 'dashboard/student_page_result.html',context=context)