from django.db import models

# Create your models here.
# пользователи,
# продукты,
# уроки в продуктах,
# статус просмотренности урока пользователем
from django.db import models


class User(models.Model):
    name = models.CharField(max_length=56)
    last_name = models.CharField(max_length=56)
    birth_date = models.DateField()


class Course(models.Model):
    title = models.TextField(max_length=156)
    user = models.ManyToManyField(User)


class Lesson(models.Model):
    title = models.TextField(max_length=156)
    parent_lesson = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)


class LessonStatus(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('lesson', 'status')
