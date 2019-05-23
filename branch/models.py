from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from accounts.models import ProfileUser, User


class Stick(models.Model):
    KIND_BRANCH_CATEGORIES = [
        ('wizzard', 'wizzard'),
        ('survakane', 'survakane'),
        ('GoodBois', 'GoodBois')
    ]
    category = models.CharField(max_length=20, choices=KIND_BRANCH_CATEGORIES, blank=True, default='unknown')
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    image_url = models.URLField(default='https://www.google.com/url?sa=i&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwjX5Z3jnZ3iAhUQEVAKHXooDSsQjRx6BAgBEAU&url=https%3A%2F%2Fwww.brazos-walking-sticks.com%2Fbackpacker-oak-walking-stick%2F&psig=AOvVaw0G4cdGjcT7wteIikom5c3B&ust=1557999287221364')
    name = models.CharField(max_length=200)
    price = models.PositiveIntegerField(validators=[MinValueValidator(10)])

    class Meta:
        abstract = True


class MagicWand(Stick):
    category = 'wizzard'
    magic_power = models.PositiveIntegerField(validators=[MaxValueValidator(9000)])

    def __str__(self):
        return f"{self.name}"


class Survachki(Stick):
    category = 'survacane'
    money_income = models.PositiveIntegerField(validators=[MinValueValidator(10)])

    def __str__(self):
        return f"{self.name}"


class Fetchers(Stick):
    category = 'GoodBois'
    barkness = models.PositiveIntegerField(validators=[MaxValueValidator(10000)])
    happiness = models.PositiveIntegerField(validators=[MinValueValidator(10000)])

    def __str__(self):
        return f"{self.name}"