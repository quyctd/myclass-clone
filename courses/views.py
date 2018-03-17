from django.shortcuts import render
from .models import Course
from django.views.generic import DetailView

# Create your views here.

class CourseDetailView(DetailView):
    model = Course
