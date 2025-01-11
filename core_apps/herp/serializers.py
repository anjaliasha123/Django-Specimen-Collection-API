from decimal import Decimal
from rest_framework import serializers
from .models import SpeciesLocation

class DecimalToFloatField(serializers.DecimalField):
    def to_representation(self, value):
        if isinstance(value, Decimal):
            return float(value)
        return super().to_representation(value)

class SpeciesLocationSerializer(serializers.ModelSerializer):
    decimal_latitude = DecimalToFloatField(max_digits=10, decimal_places=2)
    decimal_longitude = DecimalToFloatField(max_digits=10, decimal_places=2)
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
