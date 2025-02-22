# Generated by Django 5.1.4 on 2025-01-06 14:30

import django.contrib.auth.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_customuser_business_address_customuser_business_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='firstname',
            field=models.CharField(default='user', max_length=150, unique=True),
        ),
        # migrations.AddField(
        #     model_name='customuser',
        #     name='username',
        #     field=models.CharField(default='input your name', error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username'),
        #     preserve_default=False,
        # ),
        migrations.AlterField(
            model_name='customuser',
            name='business_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='directors_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
