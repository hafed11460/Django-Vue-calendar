from django.urls import path
from payments.views import PayAPIView,PackageListAPIView,PackageRetrieveAPIView,PakageAPIView
from . import views
app_name = 'payments'
urlpatterns = [

    path('', views.HomeView.as_view(), name='payment-home'),
    path('pay/<int:package_id>/', views.pay, name='pay'),
    path('state/', views.state, name='state'),
    path('testpay/', views.testpay, name='testpay'),
    # path('state/', views.StateView.as_view(), name='state'),


    path('success/', views.SuccessView.as_view(), name='success'),
    path('cancelled/', views.CancelledView.as_view(), name='cancelled'),

    #api
    path('packages/',PackageListAPIView.as_view(),name='pakages'),
    path('packages/<int:pk>/',PakageAPIView.as_view(),name='pakages-detail'),
    path('pay/',PayAPIView.as_view(),name='pay'),
]
