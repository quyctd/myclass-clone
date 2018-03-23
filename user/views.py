from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from courses.models import *
from user.forms import UserProfileForm, UserForm
# Create your views here.

def index(request):
    courses = Course.objects.all()
    context = {
        "courses" : courses,
    }
    return render(request, "homepage.html", context=context)

def signup(request):
    if request.method == 'POST':
        uform = UserCreationForm(request.POST)
        pform = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        uform = UserForm()
        pform = UserProfileForm()
    return render(request, 
                'registration/signup.html', 
                {'uform': uform, 'pform': pform}
                )
