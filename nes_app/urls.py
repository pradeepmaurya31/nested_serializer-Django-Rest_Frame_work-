from django.urls import path
from .views import Coursedetails, InstructorViewSet, CoursesViewSet, InstructordetailsView

urlpatterns = [
    path('instr/', InstructorViewSet.as_view()),
    path('course/', CoursesViewSet.as_view()),
    path('course/<int:pk>', Coursedetails.as_view(), name='course-detail'),
    path('instr/<int:pk>', InstructordetailsView.as_view(), name='instructor-detail')
]
