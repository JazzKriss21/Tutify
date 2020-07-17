from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
app_name = 'dashboard'

urlpatterns = [
    path('student/', views.student_dashboard_view, name='student_dashboard'),
    path('tutor/', views.tutor_dashboard_view, name='tutor_dashboard'),
    path('resultsearch/', views.result_search_view, name='result_search'),
]
