# Generated by Django 4.2.5 on 2023-12-20 08:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usercredentials',
            name='name',
        ),
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(max_length=10)),
                ('profile_image_path', models.CharField(blank=True, max_length=255)),
                ('occupation', models.CharField(max_length=50)),
                ('marital_status', models.CharField(max_length=20)),
                ('income', models.CharField(max_length=100)),
                ('user_credentials', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='expense.usercredentials')),
            ],
        ),
    ]
