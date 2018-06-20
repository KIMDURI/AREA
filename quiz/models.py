from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Question(models.Model):
    Q_CONTENT = models.CharField(max_length=1000, null=True)
    Q_LEVEL = models.IntegerField(default=1, null=True)
    Q_LANGUAGE= models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.Q_CONTENT

class ANSWER(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    A_CONTENT_C = models.CharField(max_length=1000)
    def __str__(self):
        return self.A_CONTENT_C

class Result(models.Model):
    result = models.IntegerField(default=0)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(timezone.now())
