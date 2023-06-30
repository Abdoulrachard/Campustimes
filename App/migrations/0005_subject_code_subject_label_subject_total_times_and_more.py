# Generated by Django 4.2.2 on 2023-06-28 11:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('App', '005_subject_create'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='code',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='subject',
            name='label',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='subject',
            name='total_times',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='timestable',
            name='classroom',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='App.classroom'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='timestable',
            name='end_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='timestable',
            name='level',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='App.level'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='timestable',
            name='start_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='timestable',
            name='subject',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='App.subject'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='timestable',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='timestable',
            name='week',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]