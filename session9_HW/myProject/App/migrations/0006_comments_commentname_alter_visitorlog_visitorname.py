# Generated by Django 4.0.4 on 2022-05-22 05:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('App', '0005_alter_visitorlog_numberview'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='commentName',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='visitorlog',
            name='visitorName',
            field=models.ForeignKey(max_length=50, on_delete=django.db.models.deletion.CASCADE, related_name='userName', to=settings.AUTH_USER_MODEL),
        ),
    ]
