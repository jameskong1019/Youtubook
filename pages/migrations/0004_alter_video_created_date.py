# Generated by Django 3.2.5 on 2021-07-12 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_alter_video_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='created_date',
            field=models.DateTimeField(editable=False),
        ),
    ]
