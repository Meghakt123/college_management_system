# Generated by Django 4.2 on 2023-06-01 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0004_notification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='subject',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='notification',
            name='updated',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
