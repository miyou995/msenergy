# Generated by Django 3.0.7 on 2020-10-18 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0028_auto_20201018_0856'),
    ]

    operations = [
        migrations.AddField(
            model_name='partenaire',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]