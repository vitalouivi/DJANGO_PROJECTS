from django.db import models


class Feedback(models.Model):
    first_name = models.CharField('Имя', max_length=20)
    last_name = models.CharField('Фамилия', max_length=20)
    company = models.CharField('Компания', max_length=20)
    email = models.CharField('Почта', max_length=20)
    cell = models.CharField('Телефон', max_length=20)
    country = models.CharField('Страна', max_length=20)
    comment = models.TextField('Комментарий')

    def __str__(self):
        return self.company

