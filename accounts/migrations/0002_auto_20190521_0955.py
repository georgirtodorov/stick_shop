# Generated by Django 2.2 on 2019-05-21 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profileuser',
            name='password',
            field=models.CharField(blank=True, default='Anon', max_length=255),
        ),
        migrations.AddField(
            model_name='profileuser',
            name='username',
            field=models.CharField(blank=True, default='Anon', max_length=255),
        ),
    ]
