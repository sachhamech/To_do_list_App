# Generated by Django 4.1 on 2022-09-14 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='To_do',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Task', models.CharField(max_length=200)),
                ('Status', models.CharField(default='incomplete', max_length=200)),
            ],
        ),
    ]
