from rest_framework.routers import DefaultRouter
from .viewsets import CourseViewSet, StudentViewSet
from django.urls import path, include

routers = DefaultRouter()

routers.register('student', StudentViewSet, 'student')
routers.register('course', CourseViewSet, 'course')

urlpatterns = [
    path('', include(routers.urls)),
]
