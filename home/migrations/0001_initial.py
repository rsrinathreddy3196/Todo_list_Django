# Generated by Django 3.2.7 on 2021-10-14 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Task_details', models.CharField(max_length=50)),
                ('Task_description', models.CharField(max_length=300)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
