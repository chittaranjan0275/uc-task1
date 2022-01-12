from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Otp(models.Model):      # OTP table for verification
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    otp = models.CharField(max_length=6, default='')

    def __str__(self):
        return self.otp

class UserType(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_verified = models.BooleanField(default=False)    #mark verified if email is veified through otp

    def __str__(self):
        return ''