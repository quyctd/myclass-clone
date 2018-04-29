from django.shortcuts import render
from .models import Course
from django.views.generic import DetailView

# Create your views here.

class CourseDetailView(DetailView):
    model = Course

def courses_list(request):
    courses = Course.objects.all()
    context = {
        "courses": courses,
    }
    return render(request, 'courses/list_all_course.html', context=context)

def categories(request, pk):
    return render(request, "courses/course_categories.html")