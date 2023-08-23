from rest_framework import serializers

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from education.models import Course, Lesson


class LessonSerializer(serializers.ModelSerializer):

    course = serializers.ReadOnlyField(source='course.title')
    lesson_owner = serializers.CharField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    lessons_count = serializers.SerializerMethodField()
    lessons = serializers.SerializerMethodField()
    lessons_info = LessonSerializer(source='course', many=True)
    course_owner = serializers.CharField(default=serializers.CurrentUserDefault())

    def get_lessons_count(self, obj):
        return obj.lessons_set.all().count()

    def get_lessons(self, obj):
        return [el.pk for el in obj.lessons.all()]

    class Meta:
        model = Course
        fields = '__all__'


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)
        token['username'] = user.username
        return token




