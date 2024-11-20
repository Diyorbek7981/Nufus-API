from django.urls import path
from .views import UsersView, FeedbackView, CreateUserView, UserGetView, CreateFeedbackView

urlpatterns = [
    path('users/', UsersView.as_view(), name='users'),
    path('feedback/', FeedbackView.as_view(), name='feedback'),
    path('create_user/', CreateUserView.as_view(), name='create'),
    path('users/<str:telegram_id>/', UserGetView.as_view(), name='user'),
    path('feedback_create/', CreateFeedbackView.as_view(), name='create_feedback'),
]
