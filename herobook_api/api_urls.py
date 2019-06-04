from django.urls import path, include


urlpatterns = [
    path('heroes/', include(('heroes.api_urls', 'heroes'))),
    path('users/', include(('accounts.api_urls', 'accounts'))),
]
