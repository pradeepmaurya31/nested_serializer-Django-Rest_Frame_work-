from .models import Instructor, Course
from .serializer import InstructorSerializer, CoursesSerializer
from rest_framework import generics


class InstructorViewSet(generics.ListCreateAPIView):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer
    
class InstructordetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer


class CoursesViewSet(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CoursesSerializer
    
    
class Coursedetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CoursesSerializer

