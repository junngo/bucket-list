# Generated by Django 2.0.9 on 2018-12-28 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bucket', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bucket',
            name='memo',
            field=models.TextField(blank=True, null=True),
        ),
    ]
