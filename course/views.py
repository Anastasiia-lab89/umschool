# Create your views here.
from django.db.models import Count
from django.http import JsonResponse
from rest_framework.viewsets import ViewSet

from course.models import LessonStatus
from course.serializers import LessonStatusSerializer


class StatusView(ViewSet):
    allowed_methods = ['post']
    serializer = LessonStatusSerializer

    def create(self, request):
        serializer = self.serializer(data=request.data)

        if serializer.is_valid():
            self.serializer.create(serializer, request.data)

            return JsonResponse({'result': 'success'})

        return JsonResponse({'result': 'error'})

    def list(self, request):
        courses_list = LessonStatus.objects.filter(
            user_id=request.query_params.get('user_id')
        ).values_list(
            'lesson__course__title'
        ).annotate(
            count=Count('lesson__course')
        )

        return JsonResponse({'result': 'success', 'data': courses_list})
