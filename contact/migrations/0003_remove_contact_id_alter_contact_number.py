# Generated by Django 4.2 on 2024-03-21 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_contact_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='id',
        ),
        migrations.AlterField(
            model_name='contact',
            name='number',
            field=models.CharField(max_length=12, primary_key=True, serialize=False, verbose_name='number'),
        ),
    ]
