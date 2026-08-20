from rest_framework import serializers
from .models import University, Course, UniversityCourse

class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class UniversityCourseSerializer(serializers.ModelSerializer):
    university_name = serializers.ReadOnlyField(source='university.name')
    course_title = serializers.ReadOnlyField(source='course.title')

    class Meta:
        model = UniversityCourse
        fields = ['id', 'university', 'university_name', 'course', 'course_title', 'semester', 'duration_weeks']
