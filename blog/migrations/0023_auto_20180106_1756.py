# Generated by Django 2.0 on 2018-01-06 12:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0022_auto_20180106_0200'),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('message', models.CharField(max_length=200)),
                ('content', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': 'News Item', 'verbose_name_plural': 'News Items'},
        ),
        migrations.AlterModelOptions(
            name='newstopic',
            options={'verbose_name': 'News Topic'},
        ),
    ]
