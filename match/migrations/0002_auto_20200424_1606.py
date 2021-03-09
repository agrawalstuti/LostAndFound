# Generated by Django 3.0.4 on 2020-04-24 10:36

from django.db import migrations, models
import match.models


class Migration(migrations.Migration):

    dependencies = [
        ('match', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='found_item',
            name='found_date',
            field=models.DateField(verbose_name='found date'),
        ),
        migrations.AlterField(
            model_name='found_item',
            name='img',
            field=models.ImageField(upload_to=match.models.UploadToPathAndRename('found_item')),
        ),
        migrations.AlterField(
            model_name='found_item',
            name='reported_date',
            field=models.DateField(auto_now_add=True, verbose_name='date reported'),
        ),
        migrations.AlterField(
            model_name='found_person',
            name='found_date',
            field=models.DateField(verbose_name='found date'),
        ),
        migrations.AlterField(
            model_name='found_person',
            name='img',
            field=models.ImageField(upload_to=match.models.UploadToPathAndRename('found_person')),
        ),
        migrations.AlterField(
            model_name='found_person',
            name='reported_date',
            field=models.DateField(auto_now_add=True, verbose_name='date reported'),
        ),
        migrations.AlterField(
            model_name='lost_item',
            name='img',
            field=models.ImageField(upload_to=match.models.UploadToPathAndRename('lost_item')),
        ),
        migrations.AlterField(
            model_name='lost_item',
            name='lost_date',
            field=models.DateField(verbose_name='lost date'),
        ),
        migrations.AlterField(
            model_name='lost_item',
            name='reported_date',
            field=models.DateField(auto_now_add=True, verbose_name='date reported'),
        ),
        migrations.AlterField(
            model_name='lost_person',
            name='img',
            field=models.ImageField(upload_to=match.models.UploadToPathAndRename('lost_person')),
        ),
        migrations.AlterField(
            model_name='lost_person',
            name='lost_date',
            field=models.DateField(verbose_name='lost date'),
        ),
        migrations.AlterField(
            model_name='lost_person',
            name='reported_date',
            field=models.DateField(auto_now_add=True, verbose_name='date reported'),
        ),
    ]
