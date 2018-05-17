from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from courses.models import *
from django.contrib.auth.models import User
from .models import UserProfile
from user.forms import SignUpForm, TeacherForm, UserProfileForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.password_validation import validate_password
from .forms import *
# Create your views here.

def index(request):
    categories = Category.objects.all()
    context = {
        "categories": categories,
    }
    return render(request, "homepage.html", context=context)

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'uform': form})

def teacher(request):
    if request.method == "POST":
        form = TeacherForm(request.POST, request.FILES)
        if form.is_valid():
            
            form.save()
            return redirect('home')
    else:
        user = request.user
        form = TeacherForm(initial={'base_info': user})
    return render(request, 'registration/teaching.html', {'form':form})

def setting(request):
    user = request.user
    if request.method == "GET":
        form = PasswordChangeCustomForm(request.user)
        return render(request, "registration/setting.html", {'form':form})
    elif request.method == "POST":
        if request.POST.get('where') == 'profile':
            first_name = request.POST.get('first_name', None)
            last_name = request.POST.get('last_name', None)
            headline = request.POST.get('headline', None)
            bio = request.POST.get('biography', None)
            if 'avatar' in request.FILES:
                avatar = request.FILES['avatar']
            else:
                avatar = None
            try:
                userprofile = UserProfile.objects.get(user = user)
            except UserProfile.DoesNotExist:
                userprofile = UserProfile.objects.create(user=user)
            if headline:
                userprofile.headline = headline
            if bio:
                userprofile.biography = bio
            if avatar:
                userprofile.avatar = avatar
            if first_name:
                user.first_name = first_name
            if last_name:
                user.last_name = last_name
            userprofile.save()
            user.save()
            return redirect('setting')
        else:
            form = PasswordChangeCustomForm(request.user, request.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)  # Important!
                messages.success(
                    request, 'Your password was successfully updated!')
                return render(request, 'registration/setting.html', {'form': form, 'success': True})

    return render(request, 'registration/setting_fail.html', {'form':form})


def my_course(request):
    user = request.user
    courses = user.course.all()
    context = {
        'courses': courses
    }
    return render(request, "courses/mycourse.html", context = context)
