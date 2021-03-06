# Generated by Django 3.1.7 on 2021-02-22 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, verbose_name='Username')),
                ('book_code', models.CharField(max_length=25, verbose_name='Book')),
                ('added_date', models.DateTimeField(auto_now_add=True, verbose_name='Added Date')),
            ],
            options={
                'verbose_name_plural': 'Bookmark List',
                'ordering': ['-added_date'],
            },
        ),
    ]
