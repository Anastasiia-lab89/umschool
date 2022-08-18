from django.contrib import admin

from course.filters import CountLessonFilter
from course.models import Lesson


# Register your models here.
# 4. необходимо сделать фильтр в админке в модели уроков по количеству просмотров, так,
# чтобы сотрудникам было удобно оценивать какие уроки неинтересны аудитории.


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_filter = (
        CountLessonFilter,
        'id',
    )
