from django.urls import path, include

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

urlpatterns = [
    path('heroes/', include(('heroes.api_urls', 'heroes'))),
    path('users/', include(('accounts.api_urls', 'users'))),
    path('authorize/', obtain_jwt_token),
    path('refresh/', refresh_jwt_token),
]
