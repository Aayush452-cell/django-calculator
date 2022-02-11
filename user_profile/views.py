from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import UserProfile
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse

def home(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        return render(request, 'home.html')


def user_signup(request):
    if request.method == 'POST':
        user_email = request.POST['email']
        username = request.POST['username']
        userpass = request.POST['password']

        try:
            user_obj = User.objects.create(username=username, email=user_email)
            user_obj.set_password(userpass)
            user_obj.save()
            user_auth = authenticate(username=username, password=userpass)
            login(request, user_auth)
            return redirect('home')
        except:
            messages.add_message(request, messages.ERROR, 'Unable to SignUp')
            return render(request, 'signup.html')

    return render(request, 'signup.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        userpass = request.POST['password']
        try:
            user_obj = authenticate(username=username, password=userpass)
            login(request, user_obj)
            request.session['username'] = username
            return redirect('home')
        except:
            messages.add_message(request, messages.ERROR, "Unable to log in.")
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


def user_logout(request):
    try:
        logout(request)
        messages.add_message(request, messages.INFO, 'You\'re logged Out!')
    except:
        messages.add_message(request, messages.ERROR, "Unable to log out.")
    return redirect('home')


def user_profile(request, user_id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            user_obj = User.objects.get(id=user_id)
            user_profiles = UserProfile.objects.filter(profile_user=request.user)
            instance = None
            if user_profiles.count() == 0:
                # user profile doesn't exist create one
                instance = UserProfile.objects.create(profile_user=request.user)
            else:
                # user profile exists
                instance = user_profiles.first()
            try:
                user_img = request.FILES['user_img']
                fs_handle = FileSystemStorage()
                img_name = 'images/user_{0}'.format(user_id)
                if fs_handle.exists(img_name):
                    fs_handle.delete(img_name)
                fs_handle.save(img_name, user_img)
                instance.profile_img = img_name
                instance.save()
                instance.refresh_from_db()
            except:
                messages.add_message(request, messages.ERROR, "Unable to update image..")
            return render(request, 'my_profile.html', {'my_profile': instance})

    if request.user.is_authenticated and request.user.id == user_id:
        try:
            user_profiles = UserProfile.objects.filter(profile_user=request.user)
            instance = None
            if user_profiles.count() == 0:
                # user profile doesn't exist create one
                instance = UserProfile.objects.create(profile_user=request.user)
            else:
                # user profile exists
                instance = user_profiles.first()
            return render(request, 'my_profile.html', {'my_profile': instance})
        except:
            return HttpResponse("It looks like some issue is there! I will get back to you shortly !!!")
    else:
        return redirect('home')
