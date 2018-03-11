from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login

# Create your views here.

def signup(request):
    if request.method == 'GET':
        form = UserCreationForm()
        return render(request, 'signup/signup.html', {'form': form})
    return HttpResponse(status=404)


# Create new Tutor
def signup_tutor(request):
    if request.method == 'GET':
        form = UserCreationForm()
        return render(request, 'signup/signup.html', {'form': form, 'user_type': 'tutor'})
        
    elif request.method == 'POST':
        form = UserCreationForm(request.POST)
        print ('tutor')
        print (request.POST)
        if form.is_valid():
            # Create the user
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')

            # Authenticate new user and add them to tutor group
            new_user = authenticate(username=username, password=raw_password)
            
            new_user.profile.user_type = 'tutor'

            # Log in new user and take them home
            login(request, new_user)
            return redirect('home')     

    return HttpResponse(status=404)


# Create new Client
def signup_client(request):
    if request.method == 'GET':
        form = UserCreationForm()
        return render(request, 'signup/signup.html', {'form': form, 'user_type': 'client'})
        
    elif request.method == 'POST':
        form = UserCreationForm(request.POST)
        print('client')
        print (request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
       
            new_user = authenticate(username=username, password=raw_password)
            new_user.profile.user_type = 'client'

            login(request, new_user)
            return redirect('home')

        print (form.errors)

    return HttpResponse(status=404)