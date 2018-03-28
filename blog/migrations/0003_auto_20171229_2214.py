# Generated by Django 2.0 on 2017-12-29 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20171229_1549'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogcomment',
            name='post',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.BlogPost'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='link',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
