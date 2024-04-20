# Generated by Django 4.2.11 on 2024-04-20 01:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Activite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=200)),
                ('date_debut', models.DateField()),
                ('date_fin', models.DateField()),
                ('lieu', models.CharField(max_length=200)),
                ('participants', models.ManyToManyField(related_name='activites', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DiscussionParentAdmin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sujet', models.CharField(max_length=200)),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('derniere_activite', models.DateTimeField(auto_now=True)),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='discussions_avec_parent', to='user.admin')),
            ],
        ),
        migrations.CreateModel(
            name='DiscussionProfAdmin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sujet', models.CharField(max_length=200)),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('derniere_activite', models.DateTimeField(auto_now=True)),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='discussions_avec_prof', to='user.admin')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenu', models.TextField()),
                ('date_envoi', models.DateTimeField(auto_now_add=True)),
                ('discussion_parent_admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parent_discussion', to='api.discussionparentadmin')),
                ('discussion_prof_admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prof_discussion', to='api.discussionprofadmin')),
            ],
        ),
        migrations.CreateModel(
            name='Matiere',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('professeurs', models.ManyToManyField(related_name='matieres', to='user.professeur')),
            ],
        ),
        migrations.AddField(
            model_name='discussionprofadmin',
            name='messages',
            field=models.ManyToManyField(related_name='messages_prof_admin', to='api.message'),
        ),
        migrations.AddField(
            model_name='discussionprofadmin',
            name='professeur',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='discussions_avec_admin', to='user.professeur'),
        ),
        migrations.AddField(
            model_name='discussionparentadmin',
            name='messages',
            field=models.ManyToManyField(related_name='messages_parent_admin', to='api.message'),
        ),
        migrations.AddField(
            model_name='discussionparentadmin',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='discussions_avec_admin', to='user.parent'),
        ),
        migrations.CreateModel(
            name='Cours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('date_debut', models.DateTimeField()),
                ('date_fin', models.DateTimeField()),
                ('est_annule', models.BooleanField(default=False)),
                ('matiere', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cours', to='api.matiere')),
                ('professeur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cours', to='user.professeur')),
            ],
        ),
        migrations.CreateModel(
            name='CommentaireCours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenu', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('cours', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentaires', to='api.cours')),
                ('matiere', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentaires', to='api.matiere')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentaires_parent', to='user.parent')),
                ('professeur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentaires_professeur', to='user.professeur')),
            ],
        ),
        migrations.CreateModel(
            name='ActiviteBloquee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('raison', models.CharField(max_length=200)),
                ('date_debut', models.DateField()),
                ('date_fin', models.DateField()),
                ('activite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.activite')),
            ],
        ),
    ]
