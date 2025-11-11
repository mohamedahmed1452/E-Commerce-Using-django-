from rest_framework import serializers
from .models import Student
from django.contrib.auth.models import User
class StudentSerializer(serializers.ModelSerializer):
    id=serializers.ReadOnlyField()
    def validate_gpa(self, value):
        if value < 0.0 or value > 4.0:
            raise serializers.ValidationError("GPA must be between 0.0 and 4.0")
        return value
    def validate_age(self, value):
        if value <= 0:
            raise serializers.ValidationError("Age must be a positive integer")
        return value
    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Name cannot be empty")
        return value
    class Meta:
        model = Student
        fields = ['id', 'name', 'age', 'gpa']
class UserSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
   
