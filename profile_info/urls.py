from django.urls import path
from . import views

app_name = 'profile_info'

urlpatterns = [
    path('student-details/',views.student_profile,name='student-profile'),
    path('tutor-details/',views.tutor_profile, name = 'tutor-profile'),
    path('<username>/', views.profile_view, name='profile'),
    path('update/<username>/', views.update_profile, name='update-profile'),
]


