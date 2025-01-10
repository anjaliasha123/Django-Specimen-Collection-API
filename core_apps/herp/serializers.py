from rest_framework import serializers
from .models import SpeciesLocation

class SpeciesLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpeciesLocation
        fields = [
            "id",
            "species_id",
            "kingdom",
            "phylum",
            "phylum_class",
            "family",
            "scientific_name",
            "genus",
            "country",
            "state_province",
            "decimal_latitude",
            "decimal_longitude",
        ]
        read_only_fields = ["id","species_id","decimal_latitude","decimal_longitude","country","state_province",]
# to allow partial updates
    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
