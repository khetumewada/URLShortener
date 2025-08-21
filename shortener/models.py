from django.db import models
from django.conf import settings
import string, random

class ShortURL(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    link = models.URLField()
    shortened = models.SlugField(unique=True, max_length=20)
    hits = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.shortened

    @staticmethod
    def generate_random_code(length=6):
        chars = string.ascii_letters + string.digits
        return ''.join(random.choices(chars, k=length))

