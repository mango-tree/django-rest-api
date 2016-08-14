from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class ServiceUser(User):
    nickname = models.CharField(max_length=30)