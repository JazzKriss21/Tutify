"""tutify URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage_view, name="home"),
    path('faq', views.faq_view, name="faq"),
    path('contact',views.contact_view, name='contact'),
    path('accounts/', include('accounts.urls',namespace="accounts"),),
    path('profile/', include("profile_info.urls", namespace="profile_info"),),
    path('dashboard/', include("dashboard.urls", namespace="dashboard"), ),

    path('friendship/', include("friendship.urls")),
    path('follow/<reciever>', views.follow_view, name='follow'),
    path('friend_request/<reciever>', views.friend_request_view, name='friend_request'),
    

    #Password resetting urls
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'),name='password_reset'),
    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),name='password_reset_complete'),

]

if settings.DEBUG: #during development you can serve user uploaded media files from media_root using the django.views.static.serve()
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)