
from django.contrib import admin
from django.urls import path, include

from core.views import index

urlpatterns = [
    path('', include('core.urls')),
    path('items/', include('items.urls')),
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),


]
