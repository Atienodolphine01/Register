# Generated by Django 3.0.6 on 2020-06-19 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_auto_20200619_1212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(db_index=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(db_index=True, max_length=30),
        ),
    ]
