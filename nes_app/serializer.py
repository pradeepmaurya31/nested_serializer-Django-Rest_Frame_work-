from .models import Instructor, Courses
from rest_framework import serializers

class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = "__all__"
        
        
class InstructorSerializer(serializers.ModelSerializer):
    course = CoursesSerializer(many=True, read_only=True)
    class Meta:
        model = Instructor
        fields = "__all__"
        
        