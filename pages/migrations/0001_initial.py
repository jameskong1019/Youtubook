# Generated by Django 3.2.4 on 2021-06-27 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subscript', models.CharField(max_length=200)),
                ('startTime', models.DecimalField(decimal_places=2, max_digits=30)),
            ],
        ),
    ]