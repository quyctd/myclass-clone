from django.shortcuts import render
from .models import Course
from django.views.generic import DetailView

# Create your views here.

class CourseDetailView(DetailView):
    model = Course

def course_list(request):
    courses = Course.objects.all()
    context = {
        "courses": courses,
    }
    return render(request, 'courses/course_list.html', context=context)