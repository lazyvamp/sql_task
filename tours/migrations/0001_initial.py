# Generated by Django 3.1.4 on 2020-12-17 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TourDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(max_length=40)),
                ('uploaded_time', models.DateField(auto_now_add=True)),
                ('city', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
                ('year', models.IntegerField()),
                ('county_name', models.CharField(max_length=10)),
                ('state_code', models.CharField(max_length=20)),
                ('state_name', models.CharField(max_length=40)),
            ],
        ),
    ]
