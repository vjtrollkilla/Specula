# Generated by Django 3.2.6 on 2021-11-04 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
