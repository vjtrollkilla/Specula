from rest_framework import serializers
from .models import Student, TimeLine
from .models import Professor

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['name','studentID','CurrentExam','CurrentAItimeStamp','CurrentAItextMessage','CurrentAIdangerLevel']

class TimeLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeLine
        fields = ['student','AItimeStamp','AItextMessage','AIdangerLevel','CurrentExam']


class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = ['name','professorID','phoneNumber','degree']

