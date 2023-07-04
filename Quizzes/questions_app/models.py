from django.db import models
from quizzes_app import Quizes
class Questions(models.Model):
    text = models.CharField(max_length=255)
    quiz = models.ForeignKey(Quizes , on_delete=models.CASCADE)
    created_at  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.text)
    
    def get_answers(self):
        return self.answer_set.all()
    

class Answer(models.Model):
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)
    question = models.ForeignKey(Questions , on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


    def get_answers(self):
        return f"Question:: {self.question.text} , answer : {self.text} , correct : {self.is_correct}"