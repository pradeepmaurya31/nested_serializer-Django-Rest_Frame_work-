from .models import Instructor, Course
from rest_framework import serializers
from django.db.models import fields

class CoursesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"
        
        
class InstructorSerializer(serializers.HyperlinkedModelSerializer):
    courses = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='course-detail')
    class Meta:
        model = Instructor
        fields = '__all__'
        