# Generated by Django 3.1.5 on 2021-01-22 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='multiplechoicequestion',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]