from django.urls import path, include
from django.contrib import admin
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(('api_urls', 'api'))),
    path('', RedirectView.as_view(pattern_name='api:heroes:list'))
]
