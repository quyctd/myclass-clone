# Generated by Django 2.0 on 2018-06-12 15:50

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '0002_auto_20150616_2121'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ten_danh_muc', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ten_khoa_hoc', models.CharField(max_length=255)),
                ('anh_cover', models.FileField(upload_to='cover/')),
                ('ngay_tao', models.DateTimeField(default=datetime.datetime(2018, 6, 12, 22, 50, 11, 897244))),
                ('mieu_ta', models.TextField()),
                ('views', models.IntegerField(default=0)),
                ('language', models.CharField(choices=[('Tiếng Việt', 'VN'), ('Tiếng Anh', 'EN')], default=('Tiếng Việt', 'VN'), max_length=64)),
                ('level', models.CharField(choices=[('Tất cả', 'All'), ('Mới học', 'Beginner'), ('Nâng cao', 'Junior')], default=('Tất cả', 'All'), max_length=64)),
                ('students', models.ManyToManyField(blank=True, related_name='course', to=settings.AUTH_USER_MODEL)),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_name', models.CharField(default='Noname', max_length=255)),
                ('link_video', models.URLField()),
                ('duration', models.DurationField(default=datetime.timedelta(0, 600))),
                ('video_id', models.CharField(max_length=255)),
                ('khoa_hoc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='video', to='courses.Course')),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='khoa_hoc',
            field=models.ManyToManyField(blank=True, related_name='categories', to='courses.Course'),
        ),
    ]
