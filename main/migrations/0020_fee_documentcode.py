# Generated by Django 4.2 on 2023-04-12 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_class_classteacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='fee',
            name='DocumentCode',
            field=models.CharField(blank=True, default=None, max_length=20, null=True),
        ),
    ]
