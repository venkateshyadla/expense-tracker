# Generated by Django 4.2.5 on 2023-12-21 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0012_expense_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetails',
            name='savings',
            field=models.IntegerField(default=0),
        ),
    ]