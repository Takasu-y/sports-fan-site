# Generated by Django 3.2.9 on 2021-12-01 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sports', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='title',
            field=models.CharField(max_length=50, null=True, verbose_name='タイトル'),
        ),
    ]