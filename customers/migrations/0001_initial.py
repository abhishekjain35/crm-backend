# Generated by Django 5.2 on 2025-04-13 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('status', models.CharField(choices=[('lead', 'Lead'), ('converted', 'Converted'), ('lost', 'Lost')], max_length=10)),
            ],
        ),
    ]
