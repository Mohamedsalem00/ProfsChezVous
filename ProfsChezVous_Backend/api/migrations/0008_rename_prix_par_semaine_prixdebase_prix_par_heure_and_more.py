# Generated by Django 5.0.6 on 2024-05-21 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_prixdebase_prix_par_eleve_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prixdebase',
            old_name='prix_par_semaine',
            new_name='prix_par_heure',
        ),
        migrations.AddField(
            model_name='prixdebase',
            name='prix_base',
            field=models.FloatField(blank=True, default=100.0, null=True),
        ),
    ]
