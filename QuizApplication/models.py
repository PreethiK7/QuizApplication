from django.db import models

# Create your models here.
class Question(models.Model):
    question_id = models.AutoField(primary_key=True)
    question_value = models.CharField(max_length=5000)

class Option(models.Model):
    option_id = models.AutoField(primary_key=True)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    option_value = models.CharField(max_length=5000)
    correct_answer = models.BooleanField(default=False)

class Result(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=500)
    score = models.IntegerField(default=0)
    percentage = models.FloatField(default=0.0)

class Quiz:
    question : Question
    options : []
