 
from rest_framework import generics
from .serializers import StaffSerializer, CarrersSerializer, PostulationSerializer
from .models import Staff, Carrers, Postulation
# Create your views here.



# Staff
class ListStaff(generics.ListAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
     
class DetailStaff(generics.RetrieveAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer


# Carrers (Job Options)
class ListCarrers(generics.ListCreateAPIView):
    queryset = Carrers.objects.all()
    serializer_class = CarrersSerializer
     
class DetailCarrers(generics.RetrieveAPIView):
    queryset = Carrers.objects.all()
    serializer_class = CarrersSerializer


# Postulation  
class ListPostulation(generics.ListCreateAPIView):
    queryset = Postulation.objects.all()
    serializer_class = PostulationSerializer
     
class DetailPostulation(generics.RetrieveAPIView):
    queryset = Postulation.objects.all()
    serializer_class = PostulationSerializer