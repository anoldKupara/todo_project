from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)  # Add this line to set a default value

    def __str__(self):
        return self.title