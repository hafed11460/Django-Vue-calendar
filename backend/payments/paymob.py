from accept.payment import *
from django.views.generic.base import TemplateView
from project import settings

class Paymob:

    def __init__(self, data):
        self.accept =  AcceptAPI(settings.PAYMOB_API_KEY)
        self.data = data
    def getAuthToken(self):
        return self.accept.retrieve_auth_token()

    def order(self,auth_token):
        OrderData = {
            "auth_token": auth_token,
            "delivery_needed": "false",
            "amount_cents": "1100",
            "currency": "EGP",
            "items": [],
        }
        return self.accept.order_registration(OrderData)

    def getPaymentToken(self):
        auth_token = self.getAuthToken()
        order = self.order(auth_token)
        Request = {
            "auth_token": auth_token,
            "amount_cents": self.data.get('product_amount'),
            "expiration": 3600,
            "order_id": order.get("id"),
            "billing_data": {
                "apartment": "803",
                "email": "claudette09@exa.com",
                "floor": "42",
                "first_name": "Clifford",
                "street": "Ethan Land",
                "building": "8028",
                "phone_number": "+86(8)9135210487",
                "shipping_method": "PKG",
                "postal_code": "01898",
                "city": "Jaskolskiburgh",
                "country": "CR",
                "last_name": "Nicolas",
                "state": "Utah"
            },
            "currency": "EGP",
            "integration_id": settings.INTEGRATION_ID,  # https://accept.paymob.com/portal2/en/PaymentIntegrations
        }
        payment_token = self.accept.payment_key_request(Request)
        print(payment_token)
        return payment_token