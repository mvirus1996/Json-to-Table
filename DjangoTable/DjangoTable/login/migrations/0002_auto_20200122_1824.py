# Generated by Django 2.2.7 on 2020-01-22 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='login',
            old_name='passwork',
            new_name='password',
        ),
    ]