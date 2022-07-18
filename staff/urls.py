from django.urls import path
from .views import *


urlpatterns = [
    path('staff', ListStaff.as_view()),
    path('staff/<int:pk>', DetailStaff.as_view()),
    
    path('jobs', ListCarrers.as_view()),
    path('jobs/<int:pk>', DetailCarrers.as_view()),

    path('postulations', ListPostulation.as_view()),
    path('postulations/<int:pk>', ListPostulation.as_view()),
    ]