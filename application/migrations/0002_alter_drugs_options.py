# Generated by Django 4.1.2 on 2022-10-09 00:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='drugs',
            options={'ordering': ['-price'], 'verbose_name': 'My-drugs'},
        ),
    ]