from urllib import request
from .models import Instructor, Course
from .serializer import InstructorSerializer, CoursesSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.authentication import BasicAuthentication


class WriteUserPermission(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        
        if request.method == 'GET':
            return True
        
        if request.method == 'POST' or request.method == 'PUT' or request.method == 'DELETE':
            if user.is_superuser:
                return True
        return False


class InstructorViewSet(generics.ListCreateAPIView):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer
    
class InstructordetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer


class CoursesViewSet(generics.ListCreateAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated,WriteUserPermission]
    queryset = Course.objects.all()
    serializer_class = CoursesSerializer
    
    
class Coursedetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CoursesSerializer

