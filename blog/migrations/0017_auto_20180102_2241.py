# Generated by Django 2.0 on 2018-01-02 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_auto_20180102_2239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='blog_covers'),
        ),
    ]
