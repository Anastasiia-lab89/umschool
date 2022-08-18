from rest_framework import serializers
from course.models import LessonStatus


class LessonStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = LessonStatus
        fields = ('lesson', 'user')

    def create(self, validated_data):

        lesson_status = LessonStatus(
            lesson_id=validated_data['lesson'],
            user_id=validated_data['user']
        )
        lesson_status.save()

        return lesson_status
