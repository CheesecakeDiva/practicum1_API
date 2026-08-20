from django.db import models

class University(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название университета")
    country = models.CharField(max_length=255, verbose_name="Страна")

    def __str__(self):
        return self.name

class Course(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название курса")
    description = models.TextField(verbose_name="Описание курса")

    def __str__(self):
        return self.title

class UniversityCourse(models.Model):
    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name="university_courses")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="course_universities")
    semester = models.CharField(max_length=50, verbose_name="Семестр")
    duration_weeks = models.PositiveIntegerField(verbose_name="Длительность в неделях")

    class Meta:
        # Курс не должен повторяться в одном семестре в конкретном университете
        constraints = [
            models.UniqueConstraint(fields=['university', 'course', 'semester'], name='unique_university_course_semester')
        ]

    def __str__(self):
        return f"{self.university.name} - {self.course.title} ({self.semester})"
