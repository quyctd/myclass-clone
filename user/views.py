from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from courses.models import *
from user.forms import SignUpForm, TeacherForm
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
        form = TeacherForm(request.POST)
        if form.is_valid():
            print(form['base_info'])
            form.save()
            return redirect('home')
    else:
        user = request.user
        form = TeacherForm(initial={'base_info': user})
    return render(request, 'registration/teaching.html', {'form':form})

def setting(request):
    user = request.user
    context = {
        "user": user,
    }
    return render(request, "registration/setting.html")
