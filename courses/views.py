from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Category, Teacher
from django.views.generic import DetailView
from django.db.models import Q
from taggit.models import Tag
import datetime
# Create your views here.

def courses_detail(request, pk):
    course = get_object_or_404(Course, pk = pk)
    time = datetime.timedelta(seconds = 0)
    for video in course.video.all():
        time += video.duration
    m, s = divmod(time.seconds, 60)
    course.views += 1
    course.save()
    if request.method == 'GET':
        suggest_course = Course.objects.all().exclude(pk = pk)[:5]
        teachers = Teacher.objects.all()[:5]
        categories = Category.objects.all()[:5]
        context = {
            "course" : course,
            "suggest_course" : suggest_course,
            "teachers" : teachers,
            "categories" : categories,
            "minutes":m,
            "seconds": s
        }
        return render(request, "courses/course_detail.html", context=context)
    elif request.method == "POST":
        user = request.user
        course.students.add(user)
        return redirect(courses_detail_enroll, pk=pk)

def courses_detail_enroll(request, pk):
    course = get_object_or_404(Course, pk=pk)
    time = datetime.timedelta(seconds=0)
    for video in course.video.all():
        time += video.duration
    m, s = divmod(time.seconds, 60)
    course.views += 1
    course.save()
    if request.method == "GET":
        suggest_course = Course.objects.all().exclude(pk=pk)[:5]
        teachers = Teacher.objects.all()[:5]
        categories = Category.objects.all()[:5]
        context = {
            "course": course,
            "suggest_course": suggest_course,
            "teachers": teachers,
            "categories": categories,
            "minutes":m,
            "seconds":s
        }
        return render(request, "courses/course_detail_enroll.html", context=context)
    elif request.method == 'POST':
        return redirect(courses_learn, pk=pk)

def courses_learn(request, pk):
    course = get_object_or_404(Course, pk=pk)
    course.views += 1
    course.save()
    context = {
        "course": course,
    }
    return render(request, "courses/course_learn.html", context=context)

def courses_list(request):
    courses = Course.objects.all()
    context = {
        "courses": courses,
    }
    return render(request, 'courses/list_all_course.html', context=context)

def categories(request, pk):
    all_cate = Category.objects.all()
    cate = get_object_or_404(Category, pk = pk)
    new_courses = Course.objects.all().order_by("-ngay_tao")[:5]
    teachers = Teacher.objects.all()[:5]

    context = {
        "categories": all_cate,
        "category" : cate,
        "new_courses": new_courses,
        "teachers" : teachers
    }
    return render(request, "courses/course_categories.html", context = context)

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
