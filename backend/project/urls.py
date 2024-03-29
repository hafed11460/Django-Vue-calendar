
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sources/', include('source.urls')),
    path('payments/', include('payments.urls')),
    path('api/', include('payments.api.urls')),
]
