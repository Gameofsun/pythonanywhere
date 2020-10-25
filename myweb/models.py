from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return f'{self.question_text}'

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.question.question_text} - {self.choice_text} - {self.votes}'


class comment(models.Model):
    namewrite = models.CharField(max_length=200)
    detail = models.CharField(max_length=1000)
    rating = models.IntegerField(default=0, max_length=10)
    def __str__(self):
        return f'{self.namewrite} - {self.detail} - {self.rating}'
