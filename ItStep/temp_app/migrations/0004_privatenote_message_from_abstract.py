# Generated by Django 4.1.6 on 2023-03-13 16:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('temp_app', '0003_message_alter_temp_options_privatemessage'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrivateNote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=15)),
                ('content', models.CharField(max_length=500)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Тексты',
                'verbose_name_plural': 'Текст',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Message_from_abstract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Сообщения',
                'verbose_name_plural': 'Сообщение',
                'abstract': False,
            },
        ),
    ]
