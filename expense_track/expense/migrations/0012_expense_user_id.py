# Generated by Django 4.2.5 on 2023-12-21 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0011_rename_category_expense_pre_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='user_id',
            field=models.CharField(default=0, max_length=20),
        ),
    ]
