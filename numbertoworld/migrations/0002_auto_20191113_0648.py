# Generated by Django 2.0.13 on 2019-11-13 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('numbertoworld', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='number',
            name='given_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]