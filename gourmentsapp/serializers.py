from rest_framework import serializers
from .models import Users, FeedbackModel


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('id', 'name', 'username', 'age', 'phone', 'gender', 'telegram_id')


class FeedbackModelSerializer(serializers.ModelSerializer):
    user = UsersSerializer(read_only=True)

    class Meta:
        model = FeedbackModel
        fields = ("id", "user", "text")


class FeedbackCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedbackModel
        fields = ("id", "user", "text")
