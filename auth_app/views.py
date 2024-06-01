from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password

from django.contrib.auth.models import User
from auth_app.models import MyUser
from dashboard.models import AdditionalSourcesModels
from tracker.views import client


# Create your views here.


def signup_view(request):
    d = {}
    if request.method == 'POST':
        data = request.POST
        username = data['username']
        email = data['email']
        password = data['password']
        region = data['region']
        signed = client.service.GetUser(username, password)

        if not User.objects.filter(username=username).exists():
            if not signed:
                user = User.objects.create_user(username, email, password)
                user.save()
                my_user = MyUser.objects.create(user=user, user_type=2)
                my_user.save()
                visited = AdditionalSourcesModels.objects.create(author=user)
                visited.save()
            else:
                user = User.objects.create_user(username, email, password, first_name=signed['Name'], )
                user.save()
                my_user = MyUser.objects.create(user=user, user_type=3, codeProject=signed['CodeProject'],
                                                code=signed['Code'], type=signed['Type'],
                                                codeSklad=signed['CodeSklad'], )
                my_user.save()
                visited = AdditionalSourcesModels.objects.create(author=user)
                visited.save()
            return redirect('/auth/login/')
        d['error'] = 'User is already exist and all fields are required'
    return render(request, '../templates/Admin/pages/samples/register-2.html', context=d)


def login_view(request):
    d = {}
    if request.method == 'POST':
        data = request.POST
        # print(data)
        username = data['username']
        password = data['password']
        signed = client.service.GetUser(username, password)
        # print(signed)
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/')
        d['error'] = 'User not found'

    return render(request, '../templates/Admin/pages/samples/login-2.html', context=d)


def lock_screen_view(request):
    d = {}
    d['user'] = MyUser.objects.filter(user=request.user).first()
    if request.method == 'POST':
        data = request.POST
        password = data['password']
        user = authenticate(request, username=request.user, password=password)
        if user:
            login(request, user)
            return redirect('/')
        d['error'] = 'Password is incorrect'
        return render(request, '../templates/Admin/pages/samples/lock-screen.html', context=d)
    if request.method == 'GET':
        return render(request, '../templates/Admin/pages/samples/lock-screen.html', context=d)


def logout_view(request):
    logout(request)
    return redirect('/auth/login')


def user_setting_view(request):
    d = {}
    d['user'] = MyUser.objects.filter(user=request.user).first()
    return render(request, '../templates/Admin/profile.html', context=d)
