from django.db import models
from django.contrib.auth.models import User

class ChatLog(models.Model):
    PHASE_CHOICES = [
        ('emphatize', 'Emphatize'),
        ('define', 'Define'),
        ('ideate', 'Ideate'),
        ('prototype', 'Prototype'),
        ('test', 'Test'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phase = models.CharField(max_length=20, choices=PHASE_CHOICES, default='emphatize')
    user_input = models.TextField()
    gpt_response = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
