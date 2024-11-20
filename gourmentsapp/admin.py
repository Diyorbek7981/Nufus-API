from django.contrib import admin
from .models import Users, FeedbackModel


# Register your models here.

@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'username', 'phone', 'gender', 'telegram_id', 'age', 'created')
    list_display_links = ('id', 'name', 'username', 'phone', 'gender', 'telegram_id', 'age', 'created')
    search_fields = ('id', 'name', 'username', 'phone', 'gender', 'telegram_id', 'age')


@admin.register(FeedbackModel)
class FeedbackModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'rate', 'created')
    list_display_links = ('id', 'user', 'rate', 'created')
    search_fields = ('id', 'user__username', 'user__name', 'rate', 'created')
