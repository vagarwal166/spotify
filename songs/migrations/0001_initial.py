# Generated by Django 4.0.5 on 2022-07-08 12:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nsme', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('artist', models.CharField(max_length=500)),
                ('time_length', models.DecimalField(blank=True, decimal_places=2, max_digits=20)),
                ('audio_file', models.FileField(upload_to='musics')),
                ('cover_image', models.ImageField(upload_to='music_image/')),
                ('album', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='songs.album')),
            ],
        ),
    ]
