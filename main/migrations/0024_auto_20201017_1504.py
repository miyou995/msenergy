# Generated by Django 3.0.7 on 2020-10-17 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_produit2'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='produit',
            options={'verbose_name': 'ProduitsB', 'verbose_name_plural': 'ProduitsB'},
        ),
        migrations.RemoveField(
            model_name='produit2',
            name='titre',
        ),
        migrations.AddField(
            model_name='produit2',
            name='ordre',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='produit2',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]