from rest_framework import serializers
from flutter.models import Teacher

class TeacherSerializer(serializers.Serializer):
    teacher_name=serializers.CharField(max_length=50)
    course_name=serializers.CharField(max_length=50)
    course_duration=serializers.IntegerField()
    seat=serializers.IntegerField()