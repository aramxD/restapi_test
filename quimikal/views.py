from rest_framework import generics
from .serializers import QuimikalSerializer
from .models import SignUp




# Create your views here.

# Comunication
class ListContact(generics.ListCreateAPIView):
    queryset = SignUp.objects.all()
    serializer_class = QuimikalSerializer
     
class DetailContact(generics.RetrieveAPIView):
    queryset = SignUp.objects.all()
    serializer_class = QuimikalSerializer