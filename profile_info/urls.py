from django.urls import path
from . import views

app_name = 'profile_info'

urlpatterns = [
    path('student-details/',views.student_profile,name='student-profile'),
    path('<username>/', views.profile_view, name='profile'),

]


