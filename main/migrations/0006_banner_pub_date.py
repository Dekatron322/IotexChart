# Generated by Django 3.2.9 on 2021-12-04 21:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_unvetted_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]