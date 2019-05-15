# Generated by Django 2.2.1 on 2019-05-15 09:43

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Survachki',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(blank=True, choices=[('wizzard', 'wizzard'), ('survakane', 'survakane'), ('GoodBois', 'GoodBois')], default='unknown', max_length=20)),
                ('image_url', models.URLField(default='https://www.google.com/url?sa=i&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwjX5Z3jnZ3iAhUQEVAKHXooDSsQjRx6BAgBEAU&url=https%3A%2F%2Fwww.brazos-walking-sticks.com%2Fbackpacker-oak-walking-stick%2F&psig=AOvVaw0G4cdGjcT7wteIikom5c3B&ust=1557999287221364')),
                ('name', models.CharField(max_length=200)),
                ('price', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(10)])),
                ('money_income', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(10)])),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.ProfileUser')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MagicWand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(blank=True, choices=[('wizzard', 'wizzard'), ('survakane', 'survakane'), ('GoodBois', 'GoodBois')], default='unknown', max_length=20)),
                ('image_url', models.URLField(default='https://www.google.com/url?sa=i&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwjX5Z3jnZ3iAhUQEVAKHXooDSsQjRx6BAgBEAU&url=https%3A%2F%2Fwww.brazos-walking-sticks.com%2Fbackpacker-oak-walking-stick%2F&psig=AOvVaw0G4cdGjcT7wteIikom5c3B&ust=1557999287221364')),
                ('name', models.CharField(max_length=200)),
                ('price', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(10)])),
                ('magic_power', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(9000)])),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.ProfileUser')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Fetchers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(blank=True, choices=[('wizzard', 'wizzard'), ('survakane', 'survakane'), ('GoodBois', 'GoodBois')], default='unknown', max_length=20)),
                ('image_url', models.URLField(default='https://www.google.com/url?sa=i&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwjX5Z3jnZ3iAhUQEVAKHXooDSsQjRx6BAgBEAU&url=https%3A%2F%2Fwww.brazos-walking-sticks.com%2Fbackpacker-oak-walking-stick%2F&psig=AOvVaw0G4cdGjcT7wteIikom5c3B&ust=1557999287221364')),
                ('name', models.CharField(max_length=200)),
                ('price', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(10)])),
                ('barkness', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(10000)])),
                ('happiness', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(10000)])),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.ProfileUser')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]