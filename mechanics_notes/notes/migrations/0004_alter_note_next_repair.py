# Generated by Django 4.0.4 on 2022-08-19 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_alter_note_next_repair_alter_note_repair'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='next_repair',
            field=models.CharField(default=None, max_length=250, null=True),
        ),
    ]
