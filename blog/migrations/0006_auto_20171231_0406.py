# Generated by Django 2.0 on 2017-12-30 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20171231_0159'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogtag',
            name='main_cat',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='event',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to='event_pictures'),
        ),
    ]
