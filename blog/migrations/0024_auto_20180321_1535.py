# Generated by Django 2.0 on 2018-03-21 10:05

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0023_auto_20180106_1756'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventInternal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('raw_link', models.CharField(blank=True, max_length=200, null=True)),
                ('date', models.CharField(blank=True, max_length=30, null=True)),
                ('subject', models.CharField(max_length=60)),
                ('location', models.CharField(blank=True, max_length=60, null=True)),
                ('processed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='MobileDataStat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_used', models.DecimalField(decimal_places=6, max_digits=12)),
                ('data_cap', models.DecimalField(decimal_places=6, max_digits=12)),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Site Meta',
                'verbose_name_plural': 'Site Meta',
            },
        ),
        migrations.CreateModel(
            name='SiteVisit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address1', models.GenericIPAddressField(null=True)),
                ('ip_address2', models.GenericIPAddressField(null=True)),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('referrer', models.CharField(max_length=150, null=True)),
                ('city', models.CharField(max_length=40, null=True)),
                ('region_code', models.CharField(max_length=4, null=True)),
                ('region', models.CharField(max_length=40, null=True)),
                ('country_name', models.CharField(max_length=40, null=True)),
                ('country', models.CharField(max_length=5, null=True)),
                ('postal', models.CharField(max_length=15, null=True)),
                ('latitude', models.DecimalField(decimal_places=4, max_digits=8, null=True)),
                ('longitude', models.DecimalField(decimal_places=4, max_digits=8, null=True)),
                ('timezone', models.CharField(max_length=30, null=True)),
                ('asn', models.CharField(max_length=15, null=True)),
                ('org', models.CharField(max_length=100, null=True)),
                ('user_agent', models.CharField(max_length=150, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SslProxy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discovered_on', models.DateTimeField(auto_now_add=True)),
                ('ip_address', models.CharField(max_length=30, unique=True)),
                ('not_working', models.BooleanField(default=False)),
                ('working', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Ssl Proxies',
            },
        ),
        migrations.CreateModel(
            name='TwitterTopic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term', models.CharField(max_length=30)),
                ('basis', models.IntegerField(default=0, help_text='0 for popularity, 1 for recent, 2 for mixed')),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='blogcomment',
            options={'verbose_name': 'Blog Comment', 'verbose_name_plural': 'Blog Comments'},
        ),
        migrations.AlterModelOptions(
            name='blogpost',
            options={'verbose_name': 'Blog Post', 'verbose_name_plural': 'Blog Posts'},
        ),
        migrations.AlterModelOptions(
            name='blogtag',
            options={'verbose_name': 'Blog Topic', 'verbose_name_plural': 'Blog Topics'},
        ),
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'User Profile', 'verbose_name_plural': 'User Profiles'},
        ),
        migrations.AddField(
            model_name='event',
            name='location',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='real_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='blogcomment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Profile'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='displayed',
            field=models.BooleanField(default=True, help_text='http://techknack.in:8000/hidden-937987398127918/<link of the post>'),
        ),
        migrations.AlterField(
            model_name='blogtag',
            name='link',
            field=models.CharField(blank=True, default='', max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='blogtag',
            name='main_cat',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='content',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_time',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='author_pic',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='content',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='link',
            field=models.CharField(max_length=400),
        ),
    ]
