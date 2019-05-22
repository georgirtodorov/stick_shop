# Generated by Django 2.2 on 2019-05-21 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20190521_0955'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profileuser',
            name='password',
        ),
        migrations.RemoveField(
            model_name='profileuser',
            name='profile_picture',
        ),
        migrations.RemoveField(
            model_name='profileuser',
            name='username',
        ),
        migrations.AddField(
            model_name='profileuser',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to='profile_pics'),
        ),
    ]