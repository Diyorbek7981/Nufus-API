from django.contrib import admin
from .models import Users, FeedbackModel, ItemModel


# Register your models here.

@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'username', 'phone', 'telegram_id', 'age', 'created')
    list_display_links = ('id', 'name', 'username', 'phone', 'telegram_id', 'age', 'created')
    search_fields = ('id', 'name', 'username', 'phone', 'telegram_id', 'age')


@admin.register(FeedbackModel)
class FeedbackModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'items', 'created')
    list_display_links = ('id', 'user', 'items', 'created')
    search_fields = ('id', 'user__username', 'user__name', 'items', 'created')


@admin.register(ItemModel)
class ItemModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'name_ru', 'created')
    list_display_links = ('id', 'name', 'name_ru', 'created')
    search_fields = ('id', 'name', 'name_ru', 'created')
