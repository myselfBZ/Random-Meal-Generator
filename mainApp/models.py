from django.db import models
from django.contrib.auth.models import User
class Meal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/', null=True)
    def __str__(self) -> str:
        return self.name
