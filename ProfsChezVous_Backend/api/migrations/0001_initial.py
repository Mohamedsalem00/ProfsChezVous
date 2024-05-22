# Generated by Django 5.0.3 on 2024-05-21 16:04

import jsonfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Absence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_absence', models.DateField()),
                ('raison', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(help_text='Nom de la catégorie', max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='CommentaireCours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenu', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('Cours_Unite', models.BooleanField()),
                ('Cours_Package', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Cours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('heure_debut', models.TimeField()),
                ('heure_fin', models.TimeField()),
                ('present', models.BooleanField(default=False)),
                ('dispense', models.BooleanField(default=False)),
                ('commentaire', models.TextField(blank=True, null=True)),
                ('montant', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Cours_Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('duree', models.PositiveIntegerField(help_text='Durée du forfait en jours')),
                ('date_debut', models.DateField(help_text='Date de début de la validité du forfait')),
                ('date_fin', models.DateField(help_text='Date de fin de la validité du forfait')),
                ('est_actif', models.BooleanField(default=False, help_text='Le forfait est-il actuellement actif ?')),
                ('nombre_semaines', models.PositiveIntegerField(choices=[(1, '1 semaine'), (2, '2 semaines'), (3, '3 semaines'), (4, '4 semaines'), (5, '5 semaines'), (6, '6 semaines'), (7, '7 semaines'), (8, '8 semaines')], help_text='Nombre de semaines')),
                ('nombre_eleves', models.PositiveIntegerField(choices=[(1, '1 élève'), (2, '2 élèves'), (3, '3 élèves'), (4, '4 élèves'), (5, '5 élèves')], help_text="Nombre d'élèves")),
                ('heures_par_semaine', models.PositiveIntegerField(default=0, help_text="Nombre d'heures par semaine")),
                ('prix', models.DecimalField(decimal_places=2, max_digits=10)),
                ('selected_disponibilites', jsonfield.fields.JSONField(blank=True, help_text='Disponibilités sélectionnées', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cours_Unite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sujet', models.TextField(max_length=100)),
                ('date', models.DateField()),
                ('heure_debut', models.TimeField(default='00:00')),
                ('duree', models.PositiveIntegerField(choices=[(60, '1 hour'), (120, '2 hours'), (180, '3 hours'), (240, '4 hours')])),
                ('statut', models.CharField(choices=[('R', 'Réservé'), ('C', 'Confirmé'), ('A', 'Annulé')], default='R', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='CoursRattrapage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_rattrapage', models.DateField()),
                ('motif', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='CoursReserve',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('heure_debut', models.TimeField()),
                ('heure_fin', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Disponibilite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=20)),
                ('heure', models.CharField(max_length=100)),
                ('est_reserve', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Evaluation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('matiere', models.CharField(max_length=100)),
                ('note', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Matiere',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_complet', models.CharField(help_text='Nom complet de la matière', max_length=150)),
                ('symbole', models.CharField(help_text='Symbole de la matière', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenu', models.TextField()),
                ('date_envoi', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('message', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('is_read', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Remboursement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motif', models.TextField()),
                ('montant_rembourse', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_demande', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='SuiviProfesseur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cours_planifies', models.IntegerField(default=0)),
                ('cours_effectues', models.IntegerField(default=0)),
                ('cours_manques', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('percentage', models.DecimalField(decimal_places=2, max_digits=5)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('success', 'Success'), ('failed', 'Failed')], max_length=20)),
            ],
        ),
    ]
