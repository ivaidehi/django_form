# Generated by Django 4.1.7 on 2023-03-09 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='reg_student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=12)),
                ('confirmPassword', models.CharField(max_length=12)),
                ('date', models.DateField()),
            ],
        ),
    ]
