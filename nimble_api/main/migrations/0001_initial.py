# Generated by Django 3.1.6 on 2023-05-11 15:43

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(default=0, help_text='We usualy order a model in a client and an admin part.', verbose_name='Sorting')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Show when an entry was created.', null=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, help_text='Show when an entry was updated', null=True, verbose_name='Updated')),
                ('is_active', models.BooleanField(default=True, help_text='This entry is visible or unvisible for a client part or admin part.', verbose_name='Public')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Delete status')),
                ('name', models.CharField(max_length=25, verbose_name='name')),
                ('description', models.TextField(blank=True, verbose_name='description')),
            ],
            options={
                'verbose_name_plural': 'Channel',
            },
        ),
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(default=0, help_text='We usualy order a model in a client and an admin part.', verbose_name='Sorting')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Show when an entry was created.', null=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, help_text='Show when an entry was updated', null=True, verbose_name='Updated')),
                ('is_active', models.BooleanField(default=True, help_text='This entry is visible or unvisible for a client part or admin part.', verbose_name='Public')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Delete status')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
            ],
            options={
                'verbose_name_plural': 'Community',
            },
        ),
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(default=0, help_text='We usualy order a model in a client and an admin part.', verbose_name='Sorting')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Show when an entry was created.', null=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, help_text='Show when an entry was updated', null=True, verbose_name='Updated')),
                ('is_active', models.BooleanField(default=True, help_text='This entry is visible or unvisible for a client part or admin part.', verbose_name='Public')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Delete status')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('description', models.TextField(blank=True, verbose_name='description')),
            ],
            options={
                'verbose_name_plural': 'Playlist',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(default=0, help_text='We usualy order a model in a client and an admin part.', verbose_name='Sorting')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Show when an entry was created.', null=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, help_text='Show when an entry was updated', null=True, verbose_name='Updated')),
                ('is_active', models.BooleanField(default=True, help_text='This entry is visible or unvisible for a client part or admin part.', verbose_name='Public')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Delete status')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
            ],
            options={
                'verbose_name_plural': 'Tag',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(default=0, help_text='We usualy order a model in a client and an admin part.', verbose_name='Sorting')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Show when an entry was created.', null=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, help_text='Show when an entry was updated', null=True, verbose_name='Updated')),
                ('is_active', models.BooleanField(default=True, help_text='This entry is visible or unvisible for a client part or admin part.', verbose_name='Public')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Delete status')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('url', models.ImageField(blank=True, null=True, upload_to=main.models.get_file_path, verbose_name='url')),
                ('views', models.IntegerField(blank=True, null=True, verbose_name='views')),
                ('category', models.PositiveIntegerField(choices=[(0, 'Education'), (1, 'Music'), (2, 'Streaming'), (3, 'Social Media'), (4, ' Gaming'), (5, 'Movie'), (6, 'Travel')], verbose_name='category')),
                ('is_private', models.BooleanField(default=False, verbose_name='is private')),
                ('like', models.PositiveIntegerField(default=0, verbose_name='common like')),
                ('value_like', models.PositiveIntegerField(default=0, verbose_name='value like')),
                ('fan_like', models.PositiveIntegerField(default=0, verbose_name='fan like')),
            ],
            options={
                'verbose_name_plural': 'Video',
            },
        ),
        migrations.CreateModel(
            name='VideoComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(default=0, help_text='We usualy order a model in a client and an admin part.', verbose_name='Sorting')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Show when an entry was created.', null=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, help_text='Show when an entry was updated', null=True, verbose_name='Updated')),
                ('is_active', models.BooleanField(default=True, help_text='This entry is visible or unvisible for a client part or admin part.', verbose_name='Public')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Delete status')),
                ('comment', models.TextField(default='')),
            ],
            options={
                'verbose_name_plural': 'VideoComment',
            },
        ),
        migrations.CreateModel(
            name='VideoLikes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(default=0, help_text='We usualy order a model in a client and an admin part.', verbose_name='Sorting')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Show when an entry was created.', null=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, help_text='Show when an entry was updated', null=True, verbose_name='Updated')),
                ('is_active', models.BooleanField(default=True, help_text='This entry is visible or unvisible for a client part or admin part.', verbose_name='Public')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Delete status')),
                ('like_type', models.PositiveIntegerField(choices=[(0, 'Common Like'), (1, 'Fan Like'), (2, 'Value Like')], default=0, verbose_name='LikeType')),
            ],
            options={
                'verbose_name_plural': 'Like',
            },
        ),
        migrations.CreateModel(
            name='VideoWatches',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(default=0, help_text='We usualy order a model in a client and an admin part.', verbose_name='Sorting')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Show when an entry was created.', null=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, help_text='Show when an entry was updated', null=True, verbose_name='Updated')),
                ('is_active', models.BooleanField(default=True, help_text='This entry is visible or unvisible for a client part or admin part.', verbose_name='Public')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Delete status')),
            ],
            options={
                'verbose_name_plural': 'VideoWatches',
            },
        ),
    ]