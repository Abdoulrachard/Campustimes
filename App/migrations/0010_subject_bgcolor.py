# Generated by Django 4.2.2 on 2023-07-01 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0009_rename_week_timestable_week_num'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='bgColor',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
