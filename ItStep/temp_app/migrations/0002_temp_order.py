# Generated by Django 4.1.6 on 2023-03-07 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('temp_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='temp',
            name='order',
            field=models.SmallIntegerField(db_index=True, default=0),
        ),
    ]