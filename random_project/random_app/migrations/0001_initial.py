# Generated by Django 4.2.11 on 2024-08-27 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Number',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('gen_date', models.DateTimeField(verbose_name='date generated')),
            ],
        ),
    ]
