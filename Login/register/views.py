from django.shortcuts import render, redirect
from employee.models import *
from register.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.urls import reverse


def register(request):
    context = {
        'form': UserRegisterForm(),
    }
    emp_obj = LeaveForm.objects.all()
    user_obj = User.objects.all()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            if User.objects.filter(email=request.POST.get('email')).count() >= 1:
                context['form'] = UserRegisterForm(request.POST)
                context['error_msg'] = 'Email already registered !!!'
                return render(request, 'register/register.html', context)
            elif LeaveForm.objects.filter(email=request.POST.get('email')).count() >= 1:
                # Process to register
                user = form.save(commit=False)
                first_name = request.POST.get('first_name')
                last_name = request.POST.get('last_name')
                email = request.POST.get('email')
                username = request.POST.get('username')
                team = request.POST.get('team')
                supervisor = request.POST.get('supervisor')
                # Check Password with Confirm Password
                if not request.POST.get('password') == request.POST.get('confirm_password'):
                    context['error_msg'] = 'Password does not match the confirm password. !!!'
                    context['form'] = UserRegisterForm(request.POST)
                    return render(request, 'register/register.html', context)
                else:
                    password = request.POST.get('password')
                    user.set_password(password)
                    form.save()
                    context['success_msg'] = 'Registration Success. !!!'
                    context['form'] = UserRegisterForm(request.POST)
                    # Save user id in LeaveForm table
                    uid_obj = User.objects.get(email=request.POST.get('email'))
                    for e in emp_obj:
                        if e.email == request.POST.get('email'):
                            e.userid = uid_obj.id
                            e.save()
                    return render(request, 'register/register.html', context)
            #else:
            #    context['form'] = UserRegisterForm(request.POST)
            #   context['error_msg'] = 'Email address does not exist. !!!'
            return render(request, 'register/register.html', context)
        elif User.objects.filter(username=request.POST.get('username')).count() >= 1:
            context['form'] = UserRegisterForm(request.POST)
            context['error_msg'] = 'Username already exists !!!'
            return render(request, 'register/register.html', context)
        else:
            context['error_msg'] = 'Invalid Email !!!'
            context['form'] = UserRegisterForm(request.POST)
            return render(request, 'register/register.html', context)
    return render(request, 'register/register.html', context)

def login_view(request):
    context = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            # return render(request, 'home.html', context)
            return HttpResponseRedirect(reverse(home_view))
        else:
            context['error_msg'] = 'Invalid username or password !!!'
            return render(request, 'register/login.html', context)
    else:
        return render(request, 'register/login.html', context)

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return HttpResponseRedirect(reverse('login'))
    return render(request, 'register/login.html', {})

@login_required(login_url="/login/")
def home_view(request):
    context = {}
    context['user'] = request.user
    return render(request, 'register/home.html', context)

@login_required(login_url="/login/")
def change_password(request):
    context = {
        'form': PasswordChangeForm(request.user, request.POST)
    }
    form = PasswordChangeForm(request.user, request.POST)
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = request.POST.get('password')
            user.set_password(password)
            form.save()
            # update_session_auth_hash(request, user)
            # messages.success(request, 'Password has been changed successfully. !!!')
            context['save_message'] = 'Password has been changed successfully. !!!'
            return render(request, 'change_password.html', context)
        else:
            # messages.error(request, 'Please correct the error below.')
            # context['error_msg'] = 'Invalid !!!'
            return render(request, 'change_password.html', {'form': form})
    return render(request, 'change_password.html', {'form': form})

