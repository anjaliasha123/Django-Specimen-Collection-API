from django.db import models


class SpeciesLocation(models.Model):
    PHYLUM_CLASS_CHOICES = [
        ('Amphibia', 'Amphibia'),
        ('Reptilia', 'Reptilia'),
    ]
    species_id = models.IntegerField()
    kingdom = models.CharField(max_length=255)
    phylum = models.CharField(max_length=255)
    phylum_class = models.CharField(max_length=255, choices=PHYLUM_CLASS_CHOICES, default='Amphibia')
    family = models.CharField(max_length=255)
    scientific_name = models.CharField(max_length=255)
    genus = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    state_province = models.CharField(max_length=255)
    decimal_latitude = models.DecimalField(max_digits=22, decimal_places=16)
    decimal_longitude = models.DecimalField(max_digits=22, decimal_places=16)

    def __str__(self):
        return self.scientific_name
    
    class Meta:
        db_table = 'species_locations'
