# Generated by Django 3.0.7 on 2020-10-20 10:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0029_partenaire_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produitdetail',
            name='gamme',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Produit2', verbose_name='catégorie gamme'),
        ),
    ]