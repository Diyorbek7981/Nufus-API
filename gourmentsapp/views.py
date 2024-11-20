from .models import Users, FeedbackModel
from .serializers import FeedbackModelSerializer, UsersSerializer, FeedbackCreateSerializer
from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class UsersView(generics.ListAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    permission_classes = [permissions.AllowAny]


class FeedbackView(generics.ListAPIView):
    queryset = FeedbackModel.objects.all()
    serializer_class = FeedbackModelSerializer
    permission_classes = [permissions.AllowAny]


class CreateUserView(generics.CreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    permission_classes = [permissions.AllowAny]


class UserGetView(APIView):
    def get(self, request, telegram_id, format=None):
        try:
            user = Users.objects.get(telegram_id=telegram_id)
        except Users.DoesNotExist:
            return Response({"detail": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        # Serialize the user data and return it in the response
        serializer = UsersSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CreateFeedbackView(generics.CreateAPIView):
    queryset = FeedbackModel.objects.all()
    serializer_class = FeedbackCreateSerializer
    permission_classes = [permissions.AllowAny]
