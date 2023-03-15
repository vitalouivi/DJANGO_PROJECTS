from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class TempManager(models.Manager):
    def get_high_to_low(self):
        return super().get_queryset().order_by('-price')

    def get_low_to_high(self):
        return super().get_queryset().order_by('price')

    def order_by_title(self):
        return super().get_queryset().order_by('title')

    def order_by_published_fresh(self):
        return super().get_queryset().order_by('-published')

    def order_by_published_old(self):
        return super().get_queryset().order_by('published')

#from temp_app.models import Temp
#Temp.objects.order_by_title()
#Temp.tmp.get_queryset()
#Temp.objects.get_high_to_low()


class Note(models.Model):
    title = models.CharField(max_length=15)
    content = models.TextField()
    email = models.EmailField()
    date = models.DateField()

    class Meta:
        verbose_name_plural = 'Текст'
        verbose_name = 'Тексты'
        abstract = True


class Note_1(Note): # Абстрактное наследование от Note
    class Meta(Note.Meta):
        pass


class PrivateNote(Note): # Абстрактное наследование от Note
    #title = models.CharField(max_length=25)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=500)
    email = None
    date = None

    class Meta(Note.Meta):
        pass


class Message_from_abstract(Note): # Абстрактное наследование от Note
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = None
    date = None
    title = None

    class Meta(Note.Meta):
        verbose_name_plural = 'Сообщение'
        verbose_name = 'Сообщения'


class Message(models.Model):
    content = models.TextField()


class PrivateMessage(Message): # Прямое наследование от Message
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #message = models.OneToOneField(Message, on_delete=models.CASCADE, parent_link=True)
    #from temp_app.models import PrivateMessage
    #from django.contrib.auth.models import User
    #usr = User.objects.get(username='1')
    #pm = PrivateMessage.objects.create(content='some text from head', user=usr)
    #pm.content
    #pm.user
    # m = pm.message_ptr
    #m.privatemessage


class Temp(models.Model):
    order = models.SmallIntegerField(default=0, db_index=True)
    title = models.CharField(max_length=50, verbose_name='Товар')
    content = models.TextField(null=True, blank=True, verbose_name='Описание')
    price = models.FloatField(null=True, blank=True, verbose_name='Цена')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')
    slug = models.SlugField("url", max_length=200, unique=True)
    objects = TempManager()
    tmp_main = models.Manager()
    tmp = TempManager()

    class Meta:
        verbose_name_plural = 'Темплэйты'
        verbose_name = 'Темплэйт'
        ordering = ['order', '-published', 'title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("temp:detail-temp", kwargs={"slug": self.slug})


class ReverseTemp(Temp): # Прокси - модель наследуемся от Temp
    #title = models.CharField() НЕ РАБОТАЕТ!!!

    class Meta:
        proxy = True
        ordering = ['-order']