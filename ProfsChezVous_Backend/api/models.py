from django.db import models
from user.models import User,Professeur, Parent , Eleve
from django.utils import timezone
from rest_framework import serializers
from django.db import models
#from .models import Cours_Package
# Dans un fichier où vous avez besoin de Cours_Package
#from api.models import Cours_Package
timezone.now
import jsonfield
from django.core.exceptions import ValidationError
from django.db.models.signals import pre_save
from django.dispatch import receiver
import datetime



class Categorie(models.Model):
    nom = models.CharField(max_length=150, help_text="Nom de la catégorie")

    def __str__(self):
        return self.nom

class Matiere(models.Model):
    nom_complet = models.CharField(max_length=150, help_text="Nom complet de la matière")
    symbole = models.CharField(max_length=50, help_text="Symbole de la matière")
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name='matieres')
    prix = models.FloatField(null=True, blank=True)
    # def to_json(self):
    #     return {
    #         'nom_complet': self.nom_complet,
    #         'symbole': self.symbole,
    #         'categorie': self.categorie.nom,
    #     }

    def __str__(self):
        return f"{self.nom_complet} - {self.symbole}"






class PrixDeBasePackage(models.Model):
    type = models.CharField(default='package',max_length=50, unique=True)
    prix_base = models.FloatField(default=100.0,null=True,blank=True)
    prix_par_heure = models.FloatField(default=100.0)
    prix_par_eleve = models.FloatField(default=50.0)

    def __str__(self):
        return self.type

class PrixDeBaseUnite(models.Model):
    type = models.CharField(default='unite',max_length=50, unique=True)
    prix_base = models.FloatField(default=100.0,null=True,blank=True)
    prix_par_heure = models.FloatField(default=100.0)
    prix_par_eleve = models.FloatField(default=50.0)

    def __str__(self):
        return self.type








class Cours_Unite(models.Model):
    sujet = models.TextField(max_length=100,null=True,blank=True)
    date_creation = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    date = models.DateField()
    heure_debut = models.TimeField(null=True,blank=False)
    heure_fine = models.TimeField(null=True, blank=False)
    STATUT_CHOICES = (
        ('R', 'Réservé'),
        ('C', 'Confirmé'),
        ('A', 'Annulé'),
    )
    nombre_eleves = models.PositiveIntegerField(choices=(
        (1, '1 élève'),
        (2, '2 élèves'),
        (3, '3 élèves'),
        (4, '4 élèves'),
        (5, '5 élèves'),
    ), help_text="Nombre d'élèves",null=True, blank=True)
    prix = models.DecimalField(max_digits=10, decimal_places=2,null=True,blank=True)
    matiere = models.ForeignKey(Matiere, on_delete=models.PROTECT, null=False)
    professeur = models.ForeignKey(Professeur, on_delete=models.SET_NULL, null=True, blank=True, related_name='cours_unite') 
    user = models.ForeignKey(User,on_delete=models.PROTECT,null=True,blank=True)
    statut = models.CharField(max_length=1, choices=STATUT_CHOICES, default='R')
    et_payer = models.BooleanField(default=False,null=True, blank=True)
    selected_disponibilites = jsonfield.JSONField(help_text="Disponibilités sélectionnées" ,null=True,blank=True)



    def __str__(self):
        return f"{self.sujet}, le {self.date}, de {self.heure_debut} à {self.heure_fine}"



class Cours_Package(models.Model):
    description = models.TextField(null=True,blank=True)
    duree = models.PositiveIntegerField(help_text="Durée du forfait en jours")
    date_creation = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    date_debut = models.DateField(help_text="Date de début de la validité du forfait")
    date_fin = models.DateField(help_text="Date de fin de la validité du forfait")
    est_actif = models.BooleanField(default=False, help_text="Le forfait est-il actuellement actif ?")
    et_payer = models.BooleanField(default=False,null=True, blank=True)
    SEMAINES_CHOICES = (
        (1, '1 semaine'),
        (2, '2 semaines'),
        (3, '3 semaines'),
        (4, '4 semaines'),
        (5, '5 semaines'),
        (6, '6 semaines'),
        (7, '7 semaines'),
        (8, '8 semaines'),
    )
    nombre_semaines = models.PositiveIntegerField(choices=SEMAINES_CHOICES, help_text="Nombre de semaines")
    nombre_eleves = models.PositiveIntegerField(choices=(
        (1, '1 élève'),
        (2, '2 élèves'),
        (3, '3 élèves'),
        (4, '4 élèves'),
        (5, '5 élèves'),
    ), help_text="Nombre d'élèves")
    STATUT_CHOICES = (
        ('R', 'Réservé'),
        ('C', 'Confirmé'),
        ('A', 'Annulé'),
    )
    statut = models.CharField(max_length=1, choices=STATUT_CHOICES, default='R')
    heures_par_semaine = models.PositiveIntegerField(help_text="Nombre d'heures par semaine", default=0)
    matiere = models.ForeignKey('Matiere', on_delete=models.PROTECT, help_text="Matière du cours")
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    selected_disponibilites = jsonfield.JSONField(help_text="Disponibilités sélectionnées" ,null=True,blank=True)
    professeur = models.ForeignKey(Professeur,on_delete=models.PROTECT, help_text="Professeur",null=True,blank=True)
    user = models.ForeignKey(User,on_delete=models.PROTECT, help_text="Parent",null=True,blank=True)
    def __str__(self):
        return f"{self.description} ({self.duree} jours), Début: {self.date_debut}, Fin: {self.date_fin}"



    

    




class Message(models.Model):
    expediteur = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages_sent')
    destinataire = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages_received')
    contenu = models.TextField()
    date_envoi = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Message : {self.contenu[:50]}..."



class Evaluation(models.Model):
    eleve = models.ForeignKey(Eleve, related_name='evaluations', on_delete=models.CASCADE)
    professeur = models.ForeignKey(Professeur, related_name='evaluations', on_delete=models.CASCADE)
    date = models.DateField()
    matiere = models.CharField(max_length=100)
    note = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"Évaluation de {self.eleve} en {self.matiere} : {self.note}" 
    
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    professeur = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transactions_prof', null=True, blank=True)
    montant = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    id_transaction = models.CharField(max_length=100, null=True, blank=True)
    montant_prof = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    montant_admin = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    date_creation = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    statut = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('success', 'Success'), ('failed', 'Failed')], null=True, blank=True)
    
    # Champs pour les relations génériques
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True, blank=True)
    object_id = models.PositiveIntegerField(null=True, blank=True)
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return f"Transaction of {self.montant} by {self.user.username} at {self.date_creation}"








# import os

# def upload_to(instance, filename):
#     # Assurez-vous que le nom du fichier est unique
#     filename_base, filename_ext = os.path.splitext(filename)
#     return f'diplomes/{instance.professeur.user.username}/{filename_base}{filename_ext}'

# class Diplome(models.Model):
#     professeur = models.ForeignKey(Professeur, on_delete=models.CASCADE)
#     fichier = models.FileField(upload_to=upload_to)

# def __str__(self):
#         return f"Diplôme de {self.professeur.user.username}"


class Cour(models.Model):
    professeur = models.ForeignKey(Professeur, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField()
    heure_debut = models.TimeField()
    heure_fin = models.TimeField()
    present = models.BooleanField(default=False)
    STATUT_CHOICES = (
        ('EC', 'En cours'),
        ('AV', 'A venir'),
        ('T', 'Terminer'),
        ('A', 'Annulé'),
    )
    statut = models.CharField(max_length=2, choices=STATUT_CHOICES, default='AV')
    dispense = models.BooleanField(default=False)
    commentaire = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Cours avec {self.professeur} le {self.date.strftime('%d %B %Y')}"
    
    @property
    def commentaires(self):
        return self.commentairecours_set.all()
    
    def update_statut(self):
        now = timezone.now()
        course_start = timezone.make_aware(datetime.datetime.combine(self.date, self.heure_debut), timezone.get_current_timezone())
        course_end = timezone.make_aware(datetime.datetime.combine(self.date, self.heure_fin), timezone.get_current_timezone())

        if course_start <= now <= course_end:
            if self.statut != 'EC':
                self.statut = 'EC'
                self.save(update_fields=['statut'])
        elif now > course_end:
            if self.statut != 'T':
                self.statut = 'T'
                self.save(update_fields=['statut'])

# @receiver(pre_save, sender=Cour)
# def mettre_a_jour_statut_cours(sender, instance, **kwargs):
#     maintenant = timezone.now()
#     heure_debut = datetime.datetime.combine(instance.date, instance.heure_debut)
#     heure_fin = datetime.datetime.combine(instance.date, instance.heure_fin)
    
#     heure_debut = timezone.make_aware(heure_debut, timezone.get_current_timezone())
#     heure_fin = timezone.make_aware(heure_fin, timezone.get_current_timezone())
    
#     if heure_debut <= maintenant <= heure_fin and instance.statut == 'AV':
#         instance.statut = 'EC'
#     elif maintenant > heure_fin and instance.statut == 'EC':
#         instance.statut = 'T'

    
class SuiviProfesseur(models.Model):
    professeur = models.OneToOneField(Professeur, on_delete=models.CASCADE)
    cours_planifies = models.IntegerField(default=0)
    cours_effectues = models.IntegerField(default=0)
    cours_manques = models.IntegerField(default=0)

    def __str__(self):
        return f"Suivi de {self.professeur}" 

class CommentaireCours(models.Model):
    contenu = models.TextField(help_text="Entrez le contenu du commentaire (entre 10 et 5000 caractères).")
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='commentaires_user', null=True, blank=True)
    cour = models.ForeignKey(Cour, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Commentaire de {self.user.get_full_name()} sur {self.cour} - {self.date.strftime('%d %B %Y')}"

    def get_short_content(self):
        """Retourne une version raccourcie du contenu du commentaire."""
        return self.contenu[:75] + ('...' if len(self.contenu) > 75 else '')

    # def clean(self):
    #     # Validation pour s'assurer qu'un utilisateur ne peut laisser qu'un commentaire par cours
    #     if CommentaireCours.objects.filter(user=self.user, cour=self.cour).exists():
    #         raise ValidationError("Vous avez déjà laissé un commentaire pour ce cours.")

    # def save(self, *args, **kwargs):
    #     # Appel de la méthode clean avant de sauvegarder
    #     self.clean()
    #     super(CommentaireCours, self).save(*args, **kwargs)

class CoursReserve(models.Model):
    professeur = models.ForeignKey(Professeur, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    heure_debut = models.TimeField()
    heure_fin = models.TimeField() 

class Absence(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_absence = models.DateField()
    raison = models.TextField()

class Remboursement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cours_manque = models.ForeignKey(Cour, on_delete=models.CASCADE)
    motif = models.TextField()
    montant_rembourse = models.DecimalField(max_digits=10, decimal_places=2)
    date_demande = models.DateField(auto_now_add=True)

class CoursRattrapage(models.Model):
    eleve = models.ForeignKey(User, on_delete=models.CASCADE)
    cours_manque = models.ForeignKey(Cour, on_delete=models.CASCADE)
    date_rattrapage = models.DateField()
    motif = models.TextField() 

    
class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    title = models.CharField(max_length=100)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def to_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'message': self.message,
            'date': self.date,
            'is_read': self.is_read
        }


    def __str__(self):
        return f"{self.title} - {self.message}"



class Disponibilite(models.Model):
    professeur = models.ForeignKey(Professeur, on_delete=models.CASCADE)
    date = models.CharField(max_length=20)  # Représente le jour de la semaine ("Lundi", "Mardi", etc.)
    heure = models.CharField(max_length=100)
    est_reserve = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.professeur} - {self.date} - {self.heure}"