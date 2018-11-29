from django.db import models

# Create your models here.
class UserData(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    address = models.CharField(max_length = 200)
    dob = models.DateField()
    weight = models.FloatField()
    height = models.FloatField()
    blood_grp = models.CharField(max_length = 5)
    def __str__(self):
        return self.first_name