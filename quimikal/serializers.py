from rest_framework import serializers
from .models import SignUp

class QuimikalSerializer(serializers.ModelSerializer):
    class Meta:
        model = SignUp
        fields = ('id', 'name','last_name', 'email','contact_number')
