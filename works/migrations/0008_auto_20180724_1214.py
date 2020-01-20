# Generated by Django 2.0.7 on 2018-07-24 12:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0007_hscnumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='hscnumber',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='hscnumber',
            name='cgst',
            field=models.FloatField(verbose_name='CGST (in %)'),
        ),
        migrations.AlterField(
            model_name='hscnumber',
            name='sgst',
            field=models.FloatField(verbose_name='SGST (in %)'),
        ),
    ]
