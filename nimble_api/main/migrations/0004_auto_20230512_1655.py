# Generated by Django 3.1.6 on 2023-05-12 10:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20230512_1625'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='url',
            new_name='video',
        ),
    ]