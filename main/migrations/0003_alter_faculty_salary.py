# Generated by Django 4.2 on 2023-04-09 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_myuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='Salary',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
    ]
