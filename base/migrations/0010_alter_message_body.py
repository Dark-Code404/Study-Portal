# Generated by Django 5.1.3 on 2025-02-24 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_message_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='body',
            field=models.TextField(blank=True, null=True),
        ),
    ]
