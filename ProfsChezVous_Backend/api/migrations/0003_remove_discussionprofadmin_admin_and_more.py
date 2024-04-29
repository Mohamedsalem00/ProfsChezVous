# Generated by Django 5.0.3 on 2024-04-29 12:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_initial'),
        ('user', '0004_delete_transaction'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='discussionprofadmin',
            name='admin',
        ),
        migrations.RemoveField(
            model_name='discussionprofadmin',
            name='messages',
        ),
        migrations.RemoveField(
            model_name='discussionprofadmin',
            name='professeur',
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
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_transactions', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='DiscussionParentAdmin',
        ),
        migrations.DeleteModel(
            name='DiscussionProfAdmin',
        ),
    ]
