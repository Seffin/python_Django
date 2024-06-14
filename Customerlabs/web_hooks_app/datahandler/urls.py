from django.urls import path
from .views import IncomingDataHandler

urlpatterns = [
    path('incoming_data/', IncomingDataHandler.as_view(), name='incoming_data'),
]