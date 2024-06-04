# Generated by Django 5.0.6 on 2024-06-01 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_transaction_content_type_transaction_object_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='cours_package',
            name='date_creation',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='cours_package',
            name='et_payer',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='cours_package',
            name='statut',
            field=models.CharField(choices=[('R', 'Réservé'), ('C', 'Confirmé'), ('A', 'Annulé')], default='R', max_length=1),
        ),
        migrations.AddField(
            model_name='cours_unite',
            name='date_creation',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='cours_unite',
            name='et_payer',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
