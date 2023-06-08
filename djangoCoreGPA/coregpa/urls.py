from django.urls import path
from .views import coreGPAView

urlpatterns = [
    path('', coreGPAView),
]