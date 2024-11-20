from django.db import models


# Create your models here.
class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Users(BaseModel):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    age = models.CharField(max_length=100)
    phone = models.CharField(max_length=100, unique=True)
    gender = models.CharField(max_length=100)
    telegram_id = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.name} ({self.username})"


class FeedbackModel(BaseModel):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='feedback')
    text = models.TextField()
    rate = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.name} {self.text[:10]}"