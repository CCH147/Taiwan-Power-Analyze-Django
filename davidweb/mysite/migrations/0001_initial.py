# Generated by Django 4.1.7 on 2023-03-27 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GHtrashData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=100)),
                ('car', models.CharField(max_length=100)),
                ('time', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ('-time',),
            },
        ),
    ]
