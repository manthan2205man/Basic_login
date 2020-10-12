from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.contrib.auth import get_user_model

class User(AbstractUser):
    is_schooladmin = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    roll_no = models.CharField(max_length=100, null=True)
    phone=models.BigIntegerField(default=0,validators=[RegexValidator(regex='\d{10}',message='invalid number',code='invalid_number')])

    def __str__(self):
        return self.first_name


class Textnotes(models.Model):
    student = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)
    textnotes = models.TextField(null=True)

    def __str__(self):
        return self.student

