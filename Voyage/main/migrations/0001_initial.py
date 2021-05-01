# Generated by Django 3.2 on 2021-05-01 14:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import main.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('room_id', models.AutoField(primary_key=True, serialize=False)),
                ('price', models.IntegerField(default=0)),
                ('details', models.CharField(default='', max_length=100)),
                ('room_desc', models.TextField(default='', max_length=1000)),
                ('address', models.TextField(default='', max_length=10000)),
                ('cover_image', models.ImageField(blank=True, null=True, upload_to=main.models.get_image_path_cover)),
                ('image_1', models.ImageField(blank=True, null=True, upload_to=main.models.get_image_path_img)),
                ('image_2', models.ImageField(blank=True, null=True, upload_to=main.models.get_image_path_img)),
                ('image_3', models.ImageField(blank=True, null=True, upload_to=main.models.get_image_path_img)),
                ('image_4', models.ImageField(blank=True, null=True, upload_to=main.models.get_image_path_img)),
                ('image_5', models.ImageField(blank=True, null=True, upload_to=main.models.get_image_path_img)),
                ('image_6', models.ImageField(blank=True, null=True, upload_to=main.models.get_image_path_img)),
                ('image_7', models.ImageField(blank=True, null=True, upload_to=main.models.get_image_path_img)),
                ('image_8', models.ImageField(blank=True, null=True, upload_to=main.models.get_image_path_img)),
                ('image_9', models.ImageField(blank=True, null=True, upload_to=main.models.get_image_path_img)),
                ('image_10', models.ImageField(blank=True, null=True, upload_to=main.models.get_image_path_img)),
                ('verified', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_id', models.IntegerField(null=True)),
                ('adults', models.IntegerField(null=True)),
                ('start', models.DateField()),
                ('end', models.DateField()),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
