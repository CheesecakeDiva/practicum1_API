from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import filters
from django.db.models import Avg, Count
from .models import University, Course, UniversityCourse
from .serializers import UniversitySerializer, CourseSerializer, UniversityCourseSerializer


class UniversityViewSet(ModelViewSet):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer
    # Поиск по названию университета
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

    @action(detail=True, methods=['get'], url_path='course-stats')
    def course_stats(self, request, pk=None):
        university = self.get_object()
        stats = university.university_courses.aggregate(
            total_courses=Count('id'),
            average_duration=Avg('duration_weeks')
        )
        return Response({
            "total_courses": stats['total_courses'] or 0,
            "average_duration": round(stats['average_duration'] or 0, 1)
        })


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']


class UniversityCourseViewSet(ModelViewSet):
    queryset = UniversityCourse.objects.all()
    serializer_class = UniversityCourseSerializer

    # Фильтрация, поиск и сортировка
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['university__name', 'course__title']
    ordering_fields = ['duration_weeks']

    def get_queryset(self):
        queryset = super().get_queryset()

        title = self.request.query_params.get('title')
        semester = self.request.query_params.get('semester')

        if title:
            queryset = queryset.filter(course__title__icontains=title)
        if semester:
            queryset = queryset.filter(semester__iexact=semester)

        return queryset

