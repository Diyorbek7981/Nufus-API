from rest_framework import serializers
from .models import Users, FeedbackModel, ItemModel


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('id', 'name', 'username', 'age', 'phone', 'telegram_id')


class ItemModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemModel
        fields = ("id", "name", "name_ru")


class FeedbackModelSerializer(serializers.ModelSerializer):
    user = UsersSerializer(read_only=True)
    items = ItemModelSerializer(read_only=True)

    class Meta:
        model = FeedbackModel
        fields = ("id", "user", "text", "items")


class FeedbackCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedbackModel
        fields = ("id", "user", "text", "items")
