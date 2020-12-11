# Generated by Django 3.1.4 on 2020-12-11 14:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('artbox_auth', '0001_initial'),
        ('art', '0005_remove_art_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='art',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='artbox_auth.userprofile'),
            preserve_default=False,
        ),
    ]