# Generated by Django 3.1.5 on 2021-02-07 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0003_multiplechoicequestion_reference'),
    ]

    operations = [
        migrations.AddField(
            model_name='multiplechoicequestion',
            name='cert_type',
            field=models.CharField(choices=[('aws_cloud_practitioner', 'AWS Cloud Practitioner'), ('aws_developer', 'AWS Certified Developer'), ('aws_solutions_architect_associate', 'AWS Solutions Architect Associate')], default='aws_cloud_practitioner', max_length=255),
        ),
    ]
