# Generated by Django 3.0.6 on 2020-06-24 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profapp', '0002_profile_is_charity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='is_charity',
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.URLField(blank=True, default='default.png'),
        ),
    ]
