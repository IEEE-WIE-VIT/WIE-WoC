from django.db import models

# Create your models here.
class Patient(models.Model):
    pid = models.IntegerField()
    name = models.CharField(max_length=100)
    contact = models.BigIntegerField()
    address = models.CharField(max_length=100)
    doc = models.CharField(max_length=100)
    ill = models.CharField(max_length=100, default="Cold")
    reference = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    class Meta:
        db_table = "p1"
        
