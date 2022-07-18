from rest_framework import serializers
from .models import Staff, Carrers, Postulation

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = ('id', 'name', 'departement','title','user_photo')


class CarrersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrers
        fields = ('id', 'name', 'description','timestamp')


class PostulationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Postulation
        fields = ('id', 'full_name', 'email', 'linkedin_url', 'portfolio_url' ,'timestamp')