# Generated by Django 3.1.6 on 2023-05-12 10:25

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20230511_2143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='url',
            field=models.FileField(blank=True, null=True, upload_to=main.models.get_file_path, verbose_name='url'),
        ),
    ]
