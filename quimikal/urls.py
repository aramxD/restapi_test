from django.urls import path
from .views import *


urlpatterns=[
    path('quimikal', ListContact.as_view()),
    path('quimikal/<int:pk>', DetailContact.as_view()),


]