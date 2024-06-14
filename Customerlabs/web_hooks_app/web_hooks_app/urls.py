from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from accounts.views import AccountViewSet
from destinations.views import DestinationViewSet
from django.http import HttpResponse

router = DefaultRouter()
router.register(r'accounts', AccountViewSet)
router.register(r'destinations', DestinationViewSet)

def index(request):
    return HttpResponse("Welcome to the Webhook Application")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('server/', include('datahandler.urls')),
    path('', index),  # Default URL pattern for the root URL
]