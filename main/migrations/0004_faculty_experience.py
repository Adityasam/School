# Generated by Django 4.2 on 2023-04-09 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_faculty_salary'),
    ]

    operations = [
        migrations.AddField(
            model_name='faculty',
            name='Experience',
            field=models.PositiveIntegerField(blank=True, default=None, null=True),
        ),
    ]
