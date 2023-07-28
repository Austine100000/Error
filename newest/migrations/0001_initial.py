# Generated by Django 4.2.3 on 2023-07-27 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('admision', models.IntegerField()),
                ('course', models.IntegerField(max_length=20)),
            ],
            options={
                'db_table': 'student',
            },
        ),
    ]
