# Generated by Django 3.2 on 2021-05-01 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(),
        ),
    ]