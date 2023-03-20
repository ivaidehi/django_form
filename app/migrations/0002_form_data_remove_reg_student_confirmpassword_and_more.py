# Generated by Django 4.1.7 on 2023-03-20 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='form_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=True, verbose_name='ID')),
                ('emailF', models.CharField(max_length=100)),
                ('studentName', models.CharField(max_length=100)),
                ('collegeName', models.CharField(max_length=100)),
                ('websiteUsername', models.CharField(max_length=100)),
                ('tasks', models.CharField(max_length=300)),
                ('percent', models.CharField(max_length=3)),
                ('date', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='reg_student',
            name='email',
            field=models.CharField(default='Null', max_length=100),
        ),
    ]
