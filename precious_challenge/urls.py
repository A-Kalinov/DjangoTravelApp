from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from trips import urls

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),
    path('admin/', admin.site.urls),
    path('api/', include(urls)),
]
