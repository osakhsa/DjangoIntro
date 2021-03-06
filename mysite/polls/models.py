import datetime
from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField('Текст вопроса', max_length=200)
    pub_date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now >= self.pub_date >= now - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = "Опубликовано недавно?"


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField('Вариант ответа', max_length=200)
    votes = models.IntegerField('Голосов', default=0)

    def __str__(self):
        return self.choice_text
