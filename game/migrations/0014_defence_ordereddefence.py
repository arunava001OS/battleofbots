# Generated by Django 3.0.1 on 2020-01-06 16:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('game', '0013_profile_weapon_list'),
    ]

    operations = [
        migrations.CreateModel(
            name='Defence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('points', models.IntegerField(default=0)),
                ('cost', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='OrderedDefence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('defence', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='game.Defence')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
