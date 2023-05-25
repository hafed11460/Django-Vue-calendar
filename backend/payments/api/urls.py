from django.urls import path
from payments.api.views import (
    PayAPIView,
    PostStateAPIView,
    PackageListAPIView,)

urlpatterns = [
    #api
    path('pay/',PayAPIView.as_view(),name='pay'),
    path('state/', PostStateAPIView.as_view(), name='state'),
    # pakages
    path('packages/',PackageListAPIView.as_view(),name='pakages'),
    # path('packages/<int:pk>/',PakageAPIView.as_view(),name='pakages-detail'),
]
