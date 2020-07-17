from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse

from accounts.forms import RegistrationForm, AccountAuthenticationForm, AccountUpdateForm


def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(username=username, password=raw_password)
            login(request, account)
            if form.cleaned_data.get('user_type')=='Student' or form.cleaned_data.get('user_type') =='student':
                return redirect(reverse('profile_info:student-profile'))
            else:
                return redirect('home')
        else:
            context['registration_form'] = form

    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'accounts/register.html', context)


def logout_view(request):
    user = request.user
    logout(request)
    return redirect('home')
    # return HttpResponse(f"Logged out {user.email}")


def login_view(request):

    context = {}

    user = request.user
    if user.is_authenticated:
        return redirect("home")
        # return HttpResponse(f"LOGGED IN {email}")


    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
                return redirect("home")
                # return HttpResponse(f"LOGGED IN {user.email}")

    else:
        form = AccountAuthenticationForm()

    context['login_form'] = form

    # print(form)
    return render(request, "accounts/login.html", context)

