from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Profile(models.Model):
    # Django add automatically an ID field. Your can also create a custom field. primary_key must be True
    GENDER = (
        ('m', 'Männlich'),
        ('w', 'Weiblich"'),
        ('d', 'Divers'),
    ) # m is the value in the database, Männlich is the Displayname, your can reach them from get_gender_display()
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)  # Here we link the user model
    # of Django,
    gender = models.CharField(max_length=1, choices=GENDER, default="d") # Gender of User, with choices
    about = models.TextField(blank=True, null=True, max_length=1000)


