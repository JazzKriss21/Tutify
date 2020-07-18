from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
app_name = 'accounts'

urlpatterns = [
    path('signup/', views.registration_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
   #Password resetting urls are in main urls.
]




