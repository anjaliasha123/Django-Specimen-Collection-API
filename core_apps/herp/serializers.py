from rest_framework import serializers
from .models import SpeciesLocation

class SpeciesLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpeciesLocation
        fields = '__all__'
# to allow partial updates
    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
