from django.shortcuts import render, get_object_or_404
from .models import Course, Category, Teacher
from django.views.generic import DetailView
from django.db.models import Q
from taggit.models import Tag
# Create your views here.


class CourseDetailView(DetailView):
    model = Course

def courses_detail(request, pk):
    course = get_object_or_404(Course, pk = pk)
    suggest_course = Course.objects.all().exclude(pk = pk)[:5]
    teachers = Teacher.objects.all()[:5]
    categories = Category.objects.all()[:5]
    context = {
        "course" : course,
        "suggest_course" : suggest_course,
        "teachers" : teachers,
        "categories" : categories
    }
    return render(request, "courses/course_detail.html", context=context)

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
