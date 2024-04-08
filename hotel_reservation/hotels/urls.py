from django.urls import path
from . import views
from .views import getAllHotels, addHotel


urlpatterns = [
    path('gethotelslist/', getAllHotels, name='get-all-hotels'),
    path('addhotel/', addHotel, name='add-hotel'),
]
