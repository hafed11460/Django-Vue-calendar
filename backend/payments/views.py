from django.shortcuts import render
from django.views.generic.base import TemplateView
from payments.paymob import Paymob
from django.shortcuts import redirect
from products.models import Package
from django.urls import reverse


def paymentView(request):
    pass

def payment(request ,pakage_id):
    if request.method == 'POST':

        # product_id = request.POST.get('product_id')
        context={}
        package = Package.objects.get(id=pakage_id)
        data = {
            'product_amount':str(package.annual_price*100)
        }
        # payment = Paymob(data=data)
        # payment_token = payment.getPaymentToken()
        context['currency'] = "EGP"
        context['package'] = package
        # context['token'] = payment_token
        # context['paymob_url']= f'https://accept.paymob.com/api/acceptance/iframes/690954?payment_token={payment_token}'
        return render(request, 'payments/payment_view.html', context=context)
    else:
        return reverse('payment-home')

class HomeView(TemplateView):
    template_name = 'payments/index.html'
    def get_context_data(self, **kwargs):
        context = {}
        context['packages'] = Package.objects.all()
        return context



class SuccessView(TemplateView):
    template_name = 'payments/success.html'


class CancelledView(TemplateView):
    template_name = 'payments/cancelled.html'