# Generated by Django 4.1.3 on 2022-12-26 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0008_slider'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
