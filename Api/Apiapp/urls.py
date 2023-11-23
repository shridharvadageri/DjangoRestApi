from django.urls import path
from .views import LaptopAllotmentPerformView

urlpatterns = [
    path('api/allotment/perform/', LaptopAllotmentPerformView.as_view(), name='laptop_allotment_perform'),
    # Other URL patterns...
]



