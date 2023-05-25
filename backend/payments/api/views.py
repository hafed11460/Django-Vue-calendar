from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from payments.paymob import Paymob
from payments.models import Subscription
from django.contrib.auth.models import User
from rest_framework.generics import ListAPIView
from payments.api.serilizers import PackageSerializer,SelectPakageSerializer
from payments.models import Package



class PayAPIView(APIView):
    def post(self, request, format=None):
        context = {}
        serializer = SelectPakageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        package_id = serializer.validated_data.get('package')
        duration = serializer.validated_data.get('duration')

        package = Package.objects.get(id=package_id)

        if duration == Subscription.SIX_MONTHS:
            amount = package.six_months_price * 100
        elif duration == Subscription.ONE_YEAR:
            amount = package.one_year_price * 100
        else:
            amount = (package.two_years_price * 100)

        data = {
            'product_amount':str(amount)
        }
        payment = Paymob(data=data)
        payment_token = payment.getPaymentToken()
        order = payment.orderData['id']

        context['paymob_url']= f'https://accept.paymob.com/api/acceptance/iframes/690954?payment_token={payment_token}'

        # ### Save order ###
        user = User.objects.all().first()
        if payment_token:
            order = Subscription.objects.create(
                        order_id = order,
                        duration = duration,
                        user= user,
                        amount=(amount/100),
                        package = package,)
        return Response(context, status=status.HTTP_200_OK)


class PostStateAPIView(APIView):

    def get(self, request, *args, **kwargs):
        return Response(request.kwargs)
    def post(self, request, *args, **kwargs):

        data = {
            "obj": {
                "id": 2556706,
                "pending": False,
                "amount_cents": 100,
                "success": True,
                "is_auth": False,
                "is_capture": False,
                "is_standalois_capturene_payment": True,
                "is_voided": False,
                "is_refunded": False,
                "is_3d_secure": True,
                "integration_id": 6741,
                "profile_id": 4214,
                "has_parent_transaction": False,
                "order": {
                "id": 4778239,
                "created_at": "2020-03-25T18:36:05.494685",
                "delivery_needed": True,
                "merchant": {
                    "id": 4214,
                    "created_at": "2019-09-22T18:32:56.764441",
                    "phones": [
                    "01032347111"
                    ],
                    "company_emails": [
                    "fnjum@temp-link.net"
                    ],
                    "company_name": "Accept Payments",
                    "state": "",
                    "country": "EGY",
                    "city": "",
                    "postal_code": "",
                    "street": ""
                },
                "collector": {
                    "id": 115,
                    "created_at": "2019-06-29T00:48:26.910433",
                    "phones": [],
                    "company_emails": [],
                    "company_name": "logix - test",
                    "state": "Heliopolis",
                    "country": "egypt",
                    "city": "cairo",
                    "postal_code": "123456",
                    "street": "Marghany"
                },
                "amount_cents": 2000,
                "shipping_data": {
                    "id": 2558893,
                    "first_name": "abdulrahman",
                    "last_name": "Khalifa",
                    "street": "Wadi el Nile",
                    "building": "5",
                    "floor": "11",
                    "apartment": "1565162",
                    "city": "Cairo",
                    "state": "Cairo",
                    "country": "EG",
                    "email": "abdulrahman@weaccept.co",
                    "phone_number": "01011994353",
                    "postal_code": "",
                    "extra_description": " ",
                    "shipping_method": "UNK",
                    "order_id": 4778239,
                    "order": 4778239
                },
                "shipping_details": {
                    "id": 1401,
                    "cash_on_delivery_amount": 0,
                    "cash_on_delivery_type": "Cash",
                    "latitude": None,
                    "longitude": None,
                    "is_same_day": 0,
                    "number_of_packages": 1,
                    "weight": 1,
                    "weight_unit": "Kilogram",
                    "length": 1,
                    "width": 1,
                    "height": 1,
                    "delivery_type": "PUD",
                    "return_type": None,
                    "order_id": 4778239,
                    "notes": "im so tired",
                    "order": 4778239
                },
                "currency": "EGP",
                "is_payment_locked": False,
                "is_return": False,
                "is_cancel": False,
                "is_returned": False,
                "is_canceled": False,
                "merchant_order_id": None,
                "wallet_notification": None,
                "paid_amount_cents": 100,
                "notify_user_with_email": False,
                "items": [],
                "order_url": "https://accept.paymobsolutions.com/i/nYWD",
                "commission_fees": 0,
                "delivery_fees_cents": 0,
                "delivery_vat_cents": 0,
                "payment_method": "tbc",
                "merchant_staff_tag": None,
                "api_source": "OTHER",
                "pickup_data": None,
                "delivery_status": []
                },
                "created_at": "2020-03-25T18:39:44.719228",
                "transaction_processed_callback_responses": [],
                "currency": "EGP",
                "source_data": {
                "pan": "2346",
                "type": "card",
                "sub_type": "MasterCard"
                },
                "api_source": "IFRAME",
                "terminal_id": None,
                "is_void": False,
                "is_refund": False,
                "data": {
                "acq_response_code": "00",
                "avs_acq_response_code": "Unsupported",
                "klass": "VPCPayment",
                "receipt_no": "008603626261",
                "order_info": "claudette09@exa.com",
                "message": "Approved",
                "gateway_integration_pk": 6741,
                "batch_no": "20200325",
                "card_num": None,
                "secure_hash": "832F4673452F9538CCD57D6B07B74183A0EEB1BEF7CA58704E31B244E8366549",
                "avs_result_code": "Unsupported",
                "card_type": "MC",
                "merchant": "TEST999999EGP",
                "created_at": "2020-03-25T16:40:37.127504",
                "merchant_txn_ref": "6741_572e773a5a0f55ff8de91876075d023e",
                "authorize_id": "626261",
                "currency": "EGP",
                "amount": "100",
                "transaction_no": "2090026774",
                "txn_response_code": "0",
                "command": "pay"
                },
                "is_hidden": False,
                "payment_key_claims": {
                "lock_order_when_paid": True,
                "integration_id": 6741,
                "billing_data": {
                    "email": "claudette09@exa.com",
                    "building": "8028",
                    "apartment": "803",
                    "street": "Ethan Land",
                    "country": "CR",
                    "state": "Utah",
                    "last_name": "Nicolas",
                    "first_name": "Clifford",
                    "postal_code": "01898",
                    "extra_description": "NA",
                    "phone_number": "+86(8)9135210487",
                    "floor": "42",
                    "city": "Jaskolskiburgh"
                },
                "order_id": 4778239,
                "user_id": 4705,
                "pmk_ip": "197.57.37.135",
                "exp": 1585157836,
                "currency": "EGP",
                "amount_cents": 100
                },
                "error_occured": False,
                "is_live": False,
                "other_endpoint_reference": None,
                "refunded_amount_cents": 0,
                "source_id": -1,
                "is_captured": False,
                "captured_amount": 0,
                "merchant_staff_tag": None,
                "owner": 4705,
                "parent_transaction": None
            },
            "type": "TRANSACTION"
            }

        order_id = data['obj']['order']['id']                       #database
        order_created_at = data['obj']['order']['created_at']
        order_merchant = data['obj']['order']['merchant']['id']
        order_items = data['obj']['order']['items']
        transaction_id = data['obj']['id']                          #database
        pending = data['obj']['pending']                            #database
        amount_cents = data['obj']['amount_cents']                  #database
        success = data['obj']['success']                            #database
        currency = data['obj']['currency']                          #database
        is_auth = data['obj']['is_auth']
        is_capture = data['obj']['is_capture']
        secure_hash = data['obj']['data']['secure_hash']            #secure hash
        # context =
        return Response(secure_hash, status=status.HTTP_200_OK)




class PackageListAPIView(ListAPIView):
    serializer_class = PackageSerializer
    queryset = Package.objects.all()