# Generated by Django 3.2.25 on 2024-08-04 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HomeApp', '0002_auto_20240804_2326'),
    ]

    operations = [
        migrations.RenameField(
            model_name='serviceweb',
            old_name='aboutUS3',
            new_name='slug',
        ),
        migrations.AlterField(
            model_name='settingweb',
            name='aboutUS2',
            field=models.TextField(blank=True, verbose_name='متن درباره ما2'),
        ),
        migrations.AlterField(
            model_name='settingweb',
            name='aboutUS3',
            field=models.TextField(blank=True, verbose_name='متن درباره ما3'),
        ),
    ]
