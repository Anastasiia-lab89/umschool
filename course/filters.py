from django.contrib import admin
from django.db.models import Count

from course.models import LessonStatus


class CountLessonFilter(admin.SimpleListFilter):
    title = 'lessons_count'
    parameter_name = 'id'

    def lookups(self, request, model_admin):
        qs = model_admin.get_queryset(request).filter(**request.GET.dict())
        for lesson_id, count in LessonStatus.objects.filter(lesson__in=qs).values_list('lesson__id').annotate(count=Count('lesson')):
            if count:
                yield (lesson_id, f'{count}')

    def queryset(self, request, queryset):
        lesson_id = self.value()
        if lesson_id:
            return queryset.filter(id=lesson_id)

        return queryset
