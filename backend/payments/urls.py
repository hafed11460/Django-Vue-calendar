from django.urls import path

from . import views

urlpatterns = [

    path('', views.HomeView.as_view(), name='payment-home'),
    path('payment/<int:pk>/', views.payment, name='payment'),
    path('success/', views.SuccessView.as_view(), name='success'),
    path('cancelled/', views.CancelledView.as_view(), name='cancelled'),
]
