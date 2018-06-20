from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Board(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)

