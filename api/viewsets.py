from re import search
from rest_framework import viewsets
from rest_framework.views import APIView
from elasticsearch_dsl import Q

from api.serializers import CourseSerializer, StudentSerializer
from .models import Course, Student
from rest_framework.response import Response


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get_serializer_class(self):
        return super().get_serializer_class()

    # get api/student/
    def list(self, request, *args, **kwargs):

        request = super().list(request, *args, **kwargs)

        return request

    def create(self, request, *args, **kwargs):

        super().create(request, *args, **kwargs)

        return Response({'message': 'New Student Create Successfully'})

    def update(self, request, *args, **kwargs):
        if 'name' in request.data:
            if request.data['name'] == 'Dwight':
                name = request.data['name']
                return Response({'message': f'Name cannot be {name}'}, status=400)
        super().update(request, *args, **kwargs)
        return Response({'message': 'Student record updated successfully'})


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
