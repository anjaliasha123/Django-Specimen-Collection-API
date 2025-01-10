from rest_framework import serializers

from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source="user.first_name")
    last_name = serializers.CharField(source="user.last_name")
    email = serializers.EmailField(source="user.email")
    full_name = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Profile
        fields = [
            "id",
            "first_name",
            "last_name",
            "full_name",
            "email",
            "country",
            "city",
            "about_me",
        ]

    def get_full_name(self, obj):
        first_name = obj.user.first_name.title()
        last_name = obj.user.first_name.title()
        return f"{first_name} {last_name}"



class UpdateProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = [
            "about_me",
            "country",
            "city",
        ]

