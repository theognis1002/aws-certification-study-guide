# Generated by Django 3.1.5 on 2021-01-19 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0004_multiplechoicequestion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(max_length=255)),
                ('answer', models.TextField()),
            ],
        ),
    ]
