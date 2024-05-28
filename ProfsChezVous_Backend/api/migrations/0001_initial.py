# Generated by Django 5.0.6 on 2024-05-24 14:58

import django.db.models.deletion
import jsonfield.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(help_text='Nom de la catégorie', max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='PrixDeBasePackage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50, unique=True)),
                ('prix_base', models.FloatField(blank=True, default=100.0, null=True)),
                ('prix_par_heure', models.FloatField(default=100.0)),
                ('prix_par_eleve', models.FloatField(default=50.0)),
            ],
        ),
        migrations.CreateModel(
            name='PrixDeBaseUnite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(default='unite', max_length=50, unique=True)),
                ('prix_base', models.FloatField(blank=True, default=100.0, null=True)),
                ('prix_par_heure', models.FloatField(default=100.0)),
                ('prix_par_eleve', models.FloatField(default=50.0)),
            ],
        ),
        migrations.CreateModel(
            name='Absence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_absence', models.DateField()),
                ('raison', models.TextField()),
                ('eleve', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
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
                ('eleve', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.eleve')),
                ('professeur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.professeur')),
            ],
        ),
        migrations.CreateModel(
            name='CoursRattrapage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_rattrapage', models.DateField()),
                ('motif', models.TextField()),
                ('cours_manque', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.cours')),
                ('eleve', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CoursReserve',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('heure_debut', models.TimeField()),
                ('heure_fin', models.TimeField()),
                ('eleve', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('professeur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.professeur')),
            ],
        ),
        migrations.CreateModel(
            name='Disponibilite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=20)),
                ('heure', models.CharField(max_length=100)),
                ('est_reserve', models.BooleanField(default=False)),
                ('professeur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.professeur')),
            ],
        ),
        migrations.CreateModel(
            name='Evaluation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('matiere', models.CharField(max_length=100)),
                ('note', models.DecimalField(decimal_places=2, max_digits=5)),
                ('eleve', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='evaluations', to='user.eleve')),
                ('professeur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='evaluations', to='user.professeur')),
            ],
        ),
        migrations.CreateModel(
            name='Matiere',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_complet', models.CharField(help_text='Nom complet de la matière', max_length=150)),
                ('symbole', models.CharField(help_text='Symbole de la matière', max_length=50)),
                ('prix', models.FloatField(blank=True, null=True)),
                ('categorie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matieres', to='api.categorie')),
            ],
        ),
        migrations.CreateModel(
            name='Cours_Unite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sujet', models.TextField(blank=True, max_length=100, null=True)),
                ('date', models.DateField()),
                ('heure_debut', models.TimeField(default='00:00')),
                ('heure_fine', models.TimeField(default='00:00', null=True)),
                ('nombre_eleves', models.PositiveIntegerField(blank=True, choices=[(1, '1 élève'), (2, '2 élèves'), (3, '3 élèves'), (4, '4 élèves'), (5, '5 élèves')], help_text="Nombre d'élèves", null=True)),
                ('prix', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('statut', models.CharField(choices=[('R', 'Réservé'), ('C', 'Confirmé'), ('A', 'Annulé')], default='R', max_length=1)),
                ('selected_disponibilites', jsonfield.fields.JSONField(blank=True, help_text='Disponibilités sélectionnées', null=True)),
                ('professeur', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cours_unite', to='user.professeur')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('matiere', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.matiere')),
            ],
        ),
        migrations.CreateModel(
            name='Cours_Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True)),
                ('duree', models.PositiveIntegerField(help_text='Durée du forfait en jours')),
                ('date_debut', models.DateField(help_text='Date de début de la validité du forfait')),
                ('date_fin', models.DateField(help_text='Date de fin de la validité du forfait')),
                ('est_actif', models.BooleanField(default=False, help_text='Le forfait est-il actuellement actif ?')),
                ('nombre_semaines', models.PositiveIntegerField(choices=[(1, '1 semaine'), (2, '2 semaines'), (3, '3 semaines'), (4, '4 semaines'), (5, '5 semaines'), (6, '6 semaines'), (7, '7 semaines'), (8, '8 semaines')], help_text='Nombre de semaines')),
                ('nombre_eleves', models.PositiveIntegerField(choices=[(1, '1 élève'), (2, '2 élèves'), (3, '3 élèves'), (4, '4 élèves'), (5, '5 élèves')], help_text="Nombre d'élèves")),
                ('heures_par_semaine', models.PositiveIntegerField(default=0, help_text="Nombre d'heures par semaine")),
                ('prix', models.DecimalField(decimal_places=2, max_digits=10)),
                ('selected_disponibilites', jsonfield.fields.JSONField(blank=True, help_text='Disponibilités sélectionnées', null=True)),
                ('professeur', models.ForeignKey(blank=True, help_text='Professeur', null=True, on_delete=django.db.models.deletion.PROTECT, to='user.professeur')),
                ('user', models.ForeignKey(blank=True, help_text='Parent', null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('matiere', models.ForeignKey(help_text='Matière du cours', on_delete=django.db.models.deletion.PROTECT, to='api.matiere')),
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
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentaires_parent', to='user.parent')),
                ('professeur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentaires_professeur', to='user.professeur')),
                ('matiere', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentaires', to='api.matiere')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenu', models.TextField()),
                ('date_envoi', models.DateTimeField(auto_now_add=True)),
                ('destinataire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages_received', to=settings.AUTH_USER_MODEL)),
                ('expediteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages_sent', to=settings.AUTH_USER_MODEL)),
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
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Remboursement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motif', models.TextField()),
                ('montant_rembourse', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_demande', models.DateField(auto_now_add=True)),
                ('cours_manque', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.cours')),
                ('eleve', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SuiviProfesseur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cours_planifies', models.IntegerField(default=0)),
                ('cours_effectues', models.IntegerField(default=0)),
                ('cours_manques', models.IntegerField(default=0)),
                ('professeur', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user.professeur')),
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
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.parent')),
                ('professeur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.professeur')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
