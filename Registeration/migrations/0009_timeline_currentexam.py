# Generated by Django 3.2.6 on 2021-11-02 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registeration', '0008_auto_20211101_1738'),
    ]

    operations = [
        migrations.AddField(
            model_name='timeline',
            name='CurrentExam',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
