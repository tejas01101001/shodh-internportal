# Generated by Django 2.2.6 on 2020-03-07 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elprofessor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accept',
            name='appl_id',
            field=models.IntegerField(default=10),
        ),
    ]
