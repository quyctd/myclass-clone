from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.views.generic import DetailView
from django.db.models import Q, Count
from taggit.models import Tag
import datetime
from django.contrib.auth import login, authenticate, update_session_auth_hash, decorators
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.contrib.auth.models import User, AnonymousUser
from .forms import *
from django.contrib import messages
from django.contrib.auth.password_validation import validate_password
from .tools import pre_upload_avatar_image
from django.db.models import F
from django.http import HttpResponseRedirect

# Create your views here.

@decorators.login_required(login_url = "/login/")
def courses_detail(request, pk):
    course = get_object_or_404(Course, pk = pk)
    time = datetime.timedelta(seconds = 0)
    for video in course.video.all():
        time += video.duration
    m, s = divmod(time.seconds, 60)
    Course.objects.filter(pk=pk).update(views=F('views') + 1)
    if request.method == 'GET':
        suggest_course = Course.objects.all().exclude(pk = pk)[:4]
        categories = Category.objects.all()[:4]
        context = {
            "course" : course,
            "suggest_course" : suggest_course,
            "categories" : categories,
            "minutes":m,
            "seconds": s
        }
        return render(request, "courses/course_detail.html", context=context)
    elif request.method == "POST":
        user = request.user
        if user.is_authenticated:
            course.students.add(user)
            return redirect(courses_detail_enroll, pk=pk)
        
def courses_detail_enroll(request, pk):
    course = get_object_or_404(Course, pk=pk)
    time = datetime.timedelta(seconds=0)
    for video in course.video.all():
        time += video.duration
    m, s = divmod(time.seconds, 60)
    Course.objects.filter(pk=pk).update(views=F('views') + 1)

    if request.method == "GET":
        suggest_course = Course.objects.all().exclude(pk=pk)[:4]
        categories = Category.objects.all()[:4]
        context = {
            "course": course,
            "suggest_course": suggest_course,
            "categories": categories,
            "minutes":m,
            "seconds":s
        }
        return render(request, "courses/course_detail_enroll.html", context=context)
    elif request.method == 'POST':
        return redirect(courses_learn, pk=pk)

def courses_learn(request, pk):
    course = get_object_or_404(Course, pk=pk)
    Course.objects.filter(pk=pk).update(views=F('views') + 1)
    context = {
        "course": course,
        "categories": Category.objects.all(),
    }
    return render(request, "courses/course_learn.html", context=context)

def courses_list(request):
    courses = Course.objects.all()
    context = {
        "courses": courses,
        "categories": Category.objects.all(),

    }
    return render(request, 'courses/list_all_course.html', context=context)

def categories(request, pk):
    all_cate = Category.objects.all()
    new_courses = Course.objects.all().order_by("-ngay_tao")[:4]

    if request.method == 'GET':
        cate = get_object_or_404(Category, pk = pk)
        courses = cate.khoa_hoc.all()
        context = {
            "categories": all_cate,
            "category" : cate,
            'courses': courses,
            "new_courses": new_courses,
        }
        return render(request, "courses/course_categories.html", context = context)

    if request.method == 'POST':
        category = request.POST.get("categories")
        sort = request.POST.get('sort')
        cate = get_object_or_404(Category, pk=int(category))
        if sort == '0':
            courses = cate.khoa_hoc.all()
        elif sort =='1':
            courses = cate.khoa_hoc.all().order_by('-ngay_tao')
        elif sort== '2':
            courses = cate.khoa_hoc.all().annotate(
                num_students=Count('students')).order_by('-num_students')
        context = {
            "categories": all_cate,
            "category": cate,
            'courses': courses,
            "new_courses": new_courses,
        }
        return render(request, "courses/course_categories.html", context=context)

def search(request):
    query = request.GET.get("q")
    if query:
        courses = Course.objects.all()
        courses = courses.filter(
            Q(ten_khoa_hoc__icontains=query)|
            Q(mieu_ta__icontains=query)
        ).distinct()
    else:
        courses = Course.objects.all()


    categories = Category.objects.all()
    tags = Tag.objects.all()
    
    context = {
        "courses": courses,
        "categories": categories,
        "tags": tags
    }
    return render(request, "search.html", context=context)


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
            next_url = request.GET.get('next', '')
            if next_url != "":
                return HttpResponseRedirect(next_url)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'uform': form})

def setting(request):
    user = request.user
    if request.method == "GET":
        form = PasswordChangeCustomForm(request.user)
        return render(request, "registration/setting.html", {'form':form, "categories": Category.objects.all()})
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

            print(avatar)
            
            
            userprofile = UserProfile.objects.filter(user = request.user).first()
            if userprofile == None:
                userprofile = UserProfile.objects.create(user=request.user, avatar = avatar, headline = "", biography = "")
            if headline:
                userprofile.headline = headline
            if bio:
                userprofile.biography = bio
            if avatar:
                userprofile.avatar = avatar
                pre_upload_avatar_image(None, userprofile)
            if first_name:
                user.first_name = first_name
            if last_name:
                user.last_name = last_name
            # UserProfile.objects.filter(user = request.user).update(views=F('views') + 1)
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
                return render(request, 'registration/setting.html', {'form': form, 'success': True, "categories": Category.objects.all()})

    context = {
        'form':form,
        "categories": Category.objects.all(),

    }
    return render(request, 'registration/setting_fail.html', context = context)


def my_course(request):
    user = request.user
    courses = user.course.all()
    context = {
        'courses': courses,
        "categories": Category.objects.all(),

    }
    return render(request, "courses/mycourse.html", context = context)
