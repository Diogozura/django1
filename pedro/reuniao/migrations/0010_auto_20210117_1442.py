# Generated by Django 3.1.5 on 2021-01-17 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reuniao', '0009_auto_20210117_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reuniao',
            name='presenca',
            field=models.CharField(choices=[('ausente', 'Ausente'), ('presenca', 'Presente')], max_length=8),
        ),
    ]