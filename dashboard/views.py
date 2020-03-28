from django.shortcuts import render

# Create your views here.

def student_dashboard_view(request):
	return render(request, 'dashboard/studentpage_afterlogin.html')

def tutor_dashboard_view(request):
	return render(request, 'dashboard/tutorpage_afterlogin.html')