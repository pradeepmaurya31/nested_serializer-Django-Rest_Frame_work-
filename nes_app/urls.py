from django.contrib import admin
from django.urls import path
from .views import InstructorViewSet, CoursesViewSet

urlpatterns = [
    path('instr', InstructorViewSet.as_view()),
    path('course', CoursesViewSet.as_view())
]
