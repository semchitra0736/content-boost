# generator/models.py
from django.db import models
from django.contrib.auth.models import User

class PromptRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    prompt_type = models.CharField(max_length=50)  # e.g., "veo3"
    user_input = models.TextField()
    result = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.prompt_type} | {self.user_input[:30]}"

