# Generated by Django 3.2.6 on 2021-08-27 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SedeModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('sede', models.CharField(db_index=True, max_length=120)),
                ('direccion', models.CharField(blank=True, max_length=255)),
                ('estado', models.IntegerField()),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
