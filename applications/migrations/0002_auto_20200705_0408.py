# Generated by Django 3.0.7 on 2020-07-05 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mynote',
            name='keyword',
        ),
        migrations.AddField(
            model_name='mynote',
            name='keyword1',
            field=models.CharField(max_length=12, null=True, verbose_name='키워드1'),
        ),
        migrations.AddField(
            model_name='mynote',
            name='keyword2',
            field=models.CharField(max_length=12, null=True, verbose_name='키워드2'),
        ),
        migrations.AddField(
            model_name='mynote',
            name='keyword3',
            field=models.CharField(max_length=12, null=True, verbose_name='키워드3'),
        ),
    ]
