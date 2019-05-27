from django.urls import path

from heroes.views import HeroDetailAPIView, HeroListAPIView


urlpatterns = [
    path('', HeroListAPIView.as_view(), name='list'),
    path('<uuid>/', HeroDetailAPIView.as_view(), name='detail'),
]
