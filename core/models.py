from django.db import models

class FAQ(models.Model):
    question = models.CharField(max_length=255, default="What is this?")
    answer = models.TextField(default="This is a default answer.")
    category = models.CharField(max_length=100, default="General")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.question
