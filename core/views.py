from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from core.models import Job
from core.tools import upload_to_center
from django.utils.crypto import get_random_string
# Create your views here.


def index(request):
    return render(request, 'index.html')


def login(request):
    if 'username' in request.session.keys():
        return render(request, 'upload.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            User.objects.get(username=username)
        except Exception:
            return render(request, 'login.html', {'error': 'No such user!'})
        user = authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            request.session['username'] = username
            return render(request, 'upload.html')
        else:
            return render(request, 'login.html', {'error': 'Incorrect password'})
    else:
        return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if username == '':
            return render(request, 'register.html', {'name_error': 'Please enter username!'})
        if password == '':
            return render(request, 'register.html', {'pass_error': 'please enter password!', 'username': username})
        try:
            User.objects.get(username=username)
        except Exception:
            User.objects.create_user(username=username, password=password)
            try:
                del request.session['username']
            except Exception:
                pass
            return render(request, 'login.html')
        return render(request, 'register.html', {'name_error': 'User already exists!'})
    else:
        return render(request, 'register.html')


def upload(request):
    x_file = request.FILES.get('x_file')
    y_file = request.FILES.get('y_file')
    if x_file is None:
        return render(request, 'upload.html', {'x_error': 'Please choose a file!'})
    if y_file is None:
        return render(request, 'upload.html', {'y_error': 'Please choose a file!'})

    x_file.name = 'x_' + get_random_string(7) + '.npy'
    y_file.name = 'y_' + get_random_string(7) + '.npy'
    Job.objects.create(
        owner=request.session['username'],
        x_file=x_file,
        y_file=y_file,
    )
    upload_to_center()
    return render(request, 'upload.html', {'success': 'Job submits successfully!'})


def logout(request):
    try:
        del request.session['username']
    except Exception:
        pass
    return render(request, 'index.html')