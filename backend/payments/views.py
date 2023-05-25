from django.shortcuts import render
from django.views.generic.base import TemplateView
from payments.paymob import Paymob
from django.shortcuts import redirect
from products.models import Package
from django.urls import reverse
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from products.serializers import PackageSerializer
from rest_framework.response import Response
from rest_framework import status


class PakageAPIView(APIView):
    def get(self, request, *args, **kwargs):
        package_id = self.kwargs.get('pk','')
        context = {}
        package =  Package.objects.get(id=package_id)
        data = {
            'product_amount':str(package.annual_price*100)
        }
        payment = Paymob(data=data)
        payment_token = payment.getPaymentToken()
        context['currency'] = "EGP"
        context['package'] = PackageSerializer(package).data
        context['token'] = payment_token
        context['paymob_url']= f'https://accept.paymob.com/api/acceptance/iframes/690954?payment_token={payment_token}'
        return Response(context, status=status.HTTP_200_OK)


class PackageRetrieveAPIView(RetrieveAPIView):

    serializer_class = PackageSerializer
    queryset = Package.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context={}
        package = self.get_object()
        # Package.objects.get(id=package_id)
        data = {
            'product_amount':str(package.annual_price*100)
        }
        payment = Paymob(data=data)
        payment_token = payment.getPaymentToken()
        context['currency'] = "EGP"
        context['package'] = package
        context['token'] = payment_token
        context['paymob_url']= f'https://accept.paymob.com/api/acceptance/iframes/690954?payment_token={payment_token}'
        return context

    def get_queryset(self):

        return super().get_queryset()


class PackageListAPIView(ListAPIView):
    serializer_class = PackageSerializer
    queryset = Package.objects.all()




class PayAPIView(APIView):
    def get(self, request, *args, **kwargs):
        pass




def paymentView(request):
    pass

def pay(request ,package_id):
    if request.method == 'POST':
        # product_id = request.POST.get('product_id')
        context={}
        package = Package.objects.get(id=package_id)
        data = {
            'product_amount':str(package.annual_price*100)
        }
        payment = Paymob(data=data)
        payment_token = payment.getPaymentToken()

        ## Store order data in DB
        context['currency'] = "EGP"
        context['package'] = package
        context['token'] = payment_token
        context['paymob_url']= f'https://accept.paymob.com/api/acceptance/iframes/690954?payment_token={payment_token}'
        return render(request, 'payments/payment_view.html', context=context)
    else:
        return reverse('payments:payment-home')

class HomeView(TemplateView):
    template_name = 'payments/index.html'
    def get_context_data(self, **kwargs):
        context = {}
        context['packages'] = Package.objects.all()
        return context



def testpay(request):
    data = request.GET
    print(data)
    _id = request.GET.get('id')
    _order  = request.GET.get('order')
    _success  = request.GET.get('success')
    _pinding  = request.GET.get('pending')
    _hmac  = request.GET.get('hmac')

    context = {}
    context['_id'] = _id # ID
    context['_order'] = _order # trans ID
    context['_success'] = _success
    context['_pinding'] = _pinding
    context['_hmac'] = _hmac

    return render(request, 'payments/testpay.html',{'data':context})



def state(request):
    data = request.get('')
    render(request, 'payments/state.html')

# class StateView(TemplateView):
#     template_name = 'payments/state.html'


class SuccessView(TemplateView):
    template_name = 'payments/success.html'


class CancelledView(TemplateView):
    template_name = 'payments/cancelled.html'