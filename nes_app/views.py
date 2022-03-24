import imp
from django.shortcuts import render
from .models import Instructor, Courses
from .serializer import InstructorSerializer, CoursesSerializer
from rest_framework import generics


class InstructorViewSet(generics.ListCreateAPIView):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer


class CoursesViewSet(generics.ListCreateAPIView):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer

