from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User
from django.db import IntegrityError
from django.contrib.auth import login

# Create your views here.

def signupuser(request):
    if request.method == 'GET':
        return render(request, 'reminderapp/signupuser.html',
                {'form' : UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'],
                                                password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('current_r')
            except IntegrityError:
                return render(request, 'reminderapp/signupuser.html',
                              {'form': UserCreationForm(),
                               'error': "This username already been taken"})
        else:
            return render(request, 'reminderapp/signupuser.html',
                          {'form': UserCreationForm(),
                           'error': "Passwords doesn't match to each other"})

def current_r(request):
    return render(request, 'reminderapp/current_r.html')


