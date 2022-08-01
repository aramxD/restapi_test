from rest_framework import generics
from .serializers import ContactSerializer
from .models import Contact




# Create your views here.

# Comunication
class ListContact(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
     
class DetailContact(generics.RetrieveAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer