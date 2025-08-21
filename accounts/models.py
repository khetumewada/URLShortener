from django.db import models
from django.contrib.auth.models import AbstractUser


class Contact(models.Model):
    title = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Feedback"


class User(AbstractUser):
    email = models.EmailField(unique=True)  # must be unique
