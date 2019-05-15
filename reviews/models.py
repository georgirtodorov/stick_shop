from django.db import models

from accounts.models import ProfileUser
from branch.models import Fetchers
# Create your models here.


class Review(models.Model):
    author = models.ForeignKey(ProfileUser, on_delete=models.CASCADE)
    content = models.TextField()
    score = models.PositiveIntegerField()
    fetcher = models.ForeignKey(Fetchers, on_delete=models.CASCADE)