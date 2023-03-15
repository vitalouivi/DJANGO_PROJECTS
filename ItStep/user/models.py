from django.db import models
from django.urls import reverse


class User(models.Model):
    #superuser = models.ForeignKey(Rubric_new, verbose_name="Рубрика2", null=True, blank=True, on_delete=models.CASCADE)
    slug = models.SlugField("username", max_length=50, unique=True)
    name = models.CharField(null=True, blank=True, max_length=30, verbose_name='Имя')
    surname = models.CharField(null=True, blank=True, max_length=30, verbose_name='Фамилия')
    date_of_birth = models.DateField(null=True, blank=True, verbose_name='Дата рождения')
    email = models.EmailField(null=True, blank=True, verbose_name='Электронная почта')
    telephone = models.CharField(null=True, blank=True, max_length=15, verbose_name='Телефон')
    registered = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Зарегистрирован')

    class Meta:
        verbose_name_plural = 'Пользователи'
        verbose_name = 'Пользователь'
        ordering = ['-registered']

    def __str__(self):
        return self.slug

    def get_absolute_url(self):
        return reverse("user:user-info", kwargs={"slug": self.slug})
