from django.db import models
from quizzes_app.models import Quizes
from django.contrib.auth.models import User


class Result(models.Model):
    quiz = models.ForeignKey(Quizes , on_delete=models.CASCADE)
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    score = models.models.FloatField()

    def __str__(self):
        return str(self.pk)