
# Register your models here.
from django.contrib import admin
from .models import SpeciesLocation
# Register your models here.

@admin.register(SpeciesLocation)
class GISFeatureAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'species_id', 'scientific_name', 'kingdom', 'phylum', 
        'phylum_class', 'family', 'genus', 'country', 
        'state_province', 'decimal_latitude', 'decimal_longitude'
    )

    list_filter = ('phylum_class', 'kingdom', 'phylum', 'country')

    search_fields = ('scientific_name', 'kingdom', 'phylum', 'phylum_class', 'id', 'country', 'state_province')
    fields = (
        'id', 'species_id','scientific_name', 'kingdom', 'phylum', 
        'phylum_class', 'family', 'genus', 'country', 
        'state_province', 'decimal_latitude', 'decimal_longitude'
    )


