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

class MovieType(models.Model):
    text = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.text}'

class Movie(models.Model):
    MovieType = models.ForeignKey(MovieType, on_delete = models.CASCADE)
    MovieName = models.CharField(max_length = 200)

    def __str__(self):
        return f'{self.MovieType} - {self.MovieName} '