# Generated by Django 4.2.7 on 2023-12-01 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='creation_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
