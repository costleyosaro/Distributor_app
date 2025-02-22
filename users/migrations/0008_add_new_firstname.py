# Generated by Django 5.1.4 on 2025-01-06 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_rename_firstname'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(max_length=30, unique=True, null=True), # important to add null=True and blank=True
        ),
    ]
