# Generated by Django 4.1.6 on 2023-02-14 17:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='username',
            new_name='slug',
        ),
    ]