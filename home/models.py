from django.db import models


# Create your models here.
class Student(models.Model):
    GENDER_TYPE = (
        ('male', 'male'),
        ('female', 'Female'),
        ('other', 'Other')
    )

    username = models.CharField(max_length=50, unique=True, default=None)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=12)
    gender = models.CharField(choices=GENDER_TYPE, max_length=8, null=True, default=None)
    email = models.EmailField(null=False, blank=False)

    def __str__(self):
        return self.email

