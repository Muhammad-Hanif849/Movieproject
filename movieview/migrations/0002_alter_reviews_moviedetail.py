# Generated by Django 4.0.1 on 2022-01-23 15:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movieview', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='moviedetail',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='movie_detail', to='movieview.moviedetail'),
        ),
    ]
