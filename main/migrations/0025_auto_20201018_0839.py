# Generated by Django 3.0.7 on 2020-10-18 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_auto_20201017_1504'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='produit2',
            options={'ordering': ['ordre'], 'verbose_name': 'Produits', 'verbose_name_plural': 'Produits'},
        ),
        migrations.AddField(
            model_name='categories_solution',
            name='ordre',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='produit2',
            name='ordre',
            field=models.IntegerField(),
        ),
    ]