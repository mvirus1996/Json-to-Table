# Generated by Django 2.2.7 on 2020-01-22 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('username', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('passwork', models.CharField(max_length=20)),
            ],
        ),
    ]
