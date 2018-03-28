# Generated by Django 2.0 on 2017-12-29 09:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_on', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='BlogEmbed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.FileField(upload_to='blog_embeds')),
            ],
        ),
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField()),
                ('title', models.CharField(max_length=200)),
                ('cover', models.ImageField(null=True, upload_to='blog_covers')),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('publish_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('displayed', models.BooleanField(default=True)),
                ('content', models.TextField(null=True)),
                ('snippet', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='BlogTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('link', models.URLField()),
                ('post', models.ManyToManyField(related_name='tags', to='blog.BlogPost')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=50, null=True)),
                ('content', models.CharField(max_length=150)),
                ('event_time', models.DateTimeField()),
                ('publish_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('displayed', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='NavTabs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('link', models.URLField()),
                ('glyphicon', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_name', models.CharField(max_length=40, null=True)),
                ('link', models.URLField()),
                ('content', models.CharField(max_length=150)),
                ('posted_on', models.DateTimeField()),
                ('publish_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('displayed', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('avatar', models.ImageField(upload_to='user_avatars')),
                ('role', models.IntegerField(default=0)),
                ('link', models.URLField(null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ReadLater',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='blog.BlogPost')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=40)),
                ('author_handle', models.CharField(max_length=40)),
                ('author_pic', models.ImageField(null=True, upload_to='twitter_dps')),
                ('link', models.URLField()),
                ('content', models.CharField(max_length=150)),
                ('posted_on', models.DateTimeField()),
                ('publish_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('displayed', models.BooleanField(default=True)),
            ],
        ),
        migrations.AddField(
            model_name='blogpost',
            name='authors',
            field=models.ManyToManyField(to='blog.Profile'),
        ),
        migrations.AddField(
            model_name='blogembed',
            name='blog',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.BlogPost'),
        ),
        migrations.AddField(
            model_name='blogcomment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='blog.Profile'),
        ),
    ]
