# Generated by Django 3.2.6 on 2021-08-20 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('txtName', models.CharField(max_length=200)),
                ('txtEmail', models.EmailField(max_length=254)),
                ('txtPhone', models.CharField(max_length=15)),
                ('txtMsg', models.TextField()),
            ],
        ),
    ]
