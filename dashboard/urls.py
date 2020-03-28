from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('student/', views.student_dashboard_view, name='student_dashboard'),
    path('tutor/', views.tutor_dashboard_view, name='tutor_dashboard'),
]
