from django.contrib import admin

from .models import Question, Choice, MovieType, Movie

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(MovieType)
admin.site.register(Movie)

