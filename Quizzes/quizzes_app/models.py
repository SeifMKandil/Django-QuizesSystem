from django.db import models

DIFF_CHOICES = (
    ('easy' , 'easy'),
    ('medium' , 'medium'),
    ('hard' , 'hard'),
    
)
class Quizes (models.Model):
    name = models.CharField(max_length=50)
    topic = models.CharField(max_length=50)
    number_of_questions = models.IntegerField()
    duration = models.IntegerField(help_text="Duration in minutes")
    pass_score = models.IntegerField(help_text="Score in %")
    difficulty = models.CharField(max_length=6  ,choices=DIFF_CHOICES)

    def __str__(self):
        return f"{self.name}-{self.topic}"
    
    def get_questions(self):
        return self.questions_set.all(0)
    
    class Meta:
        verbose_name_plural = "Quizes" 