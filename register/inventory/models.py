from django.db import models

class Equipment(models.Model):
    photo = models.ImageField(upload_to='photos/', null=True, blank=True)
    name = models.CharField(max_length=200)
    dimension1 = models.FloatField(null=True, blank=True)
    dimension2 = models.FloatField(null=True, blank=True)
    dimension3 = models.FloatField(null=True, blank=True)
    supplier_art = models.CharField(max_length=200, null=True, blank=True)
    quantity = models.IntegerField(default=0)
    storage_location = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name
