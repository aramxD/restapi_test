from django.urls import path
from .views import *


urlpatterns=[
    path('contact', ListContact.as_view()),
    path('contact/<int:pk>', DetailContact.as_view()),


]