# Generated by Django 2.0 on 2018-01-03 06:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_mediafiles'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to='news_pics'),
        ),
        migrations.AlterField(
            model_name='blogembed',
            name='blog',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='blog.BlogPost'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='user_avatars'),
        ),
    ]
