# Generated by Django 3.1 on 2020-09-27 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20200924_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories_solution',
            name='image',
            field=models.ImageField(blank=True, upload_to='slides/'),
        ),
    ]
