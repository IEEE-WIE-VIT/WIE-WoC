from django.db import models

# Create your models here.


class addDetails(models.Model):
    idno = models.CharField(max_length=100)
    phno = models.CharField(max_length=100)
    equipment_type = models.CharField(max_length=100)
    noOfitems = models.IntegerField()
    times = models.TimeField()
    isAccepted = models.BooleanField(default=False)







