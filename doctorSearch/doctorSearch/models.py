from django.db import models

class doctor(models.Model):
    name = models.CharField(max_length=255)
    specialty = models.CharField(max_length=255)
    area = models.CharField(max_length=255)
    reviewScore = models.IntegerField()
    
   
    def __str__(self):
        return self.name