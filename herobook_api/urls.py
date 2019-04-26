from django.urls import path

from heroes.views import HeroListAPIView, HeroDetailAPIView

urlpatterns = [
    path('api/v1/heroes/', HeroListAPIView.as_view(), name='heroes'),
    path('api/v1/heroes/<int:id>', HeroDetailAPIView.as_view(), name='hero-detail'),
]
