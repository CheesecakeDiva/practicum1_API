from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('universities', views.UniversityViewSet, basename='university')
router.register('courses', views.CourseViewSet, basename='course')
router.register('university-courses', views.UniversityCourseViewSet, basename='universitycourse')

urlpatterns = [
    path('', include(router.urls)),
]
