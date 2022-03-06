from django.db import models
from django.contrib.auth import get_user_model


# Create your models here
class Student(models.Model):
    GENDER_TYPE = (
        ('male', 'male'),
        ('female', 'Female'),
        ('other', 'Other')
    )

    email = models.EmailField(null=False, blank=False, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=12)
    gender = models.CharField(choices=GENDER_TYPE, max_length=8, null=True, default=None)
    standard = models.IntegerField(null=False, default=10)
    roll_number = models.IntegerField(null=False, default=None)

    class Meta:
        unique_together = ("standard", "roll_number")

    def __str__(self):
        return self.email
