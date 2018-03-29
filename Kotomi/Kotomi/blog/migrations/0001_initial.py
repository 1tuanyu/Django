# Generated by Django 2.0.3 on 2018-03-26 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='标题')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='发布日期')),
                ('lable', models.CharField(blank=True, max_length=30, verbose_name='标签')),
                ('content', models.TextField(null=True, verbose_name='正文')),
            ],
        ),
    ]