# Generated by Django 3.2.4 on 2021-06-07 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='jjcuser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Email', models.CharField(max_length=200)),
                ('variety', models.CharField(max_length=200)),
                ('messg', models.TextField(blank=True)),
                ('display', models.TextField(blank=True)),
            ],
        ),
    ]
