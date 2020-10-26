# -*- coding: utf-8 -*-
import logging
import os
import json

from django.shortcuts import render
from django.conf import settings
from django.views import generic

import stripe
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt

logger = logging.getLogger(__name__)

# Create your views here.
class IndexView(generic.TemplateView):
    template_name = "checkout/checkout_test.html"
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name )

class SuccessView(generic.TemplateView):
    template_name = "checkout/success.html"
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name )

class CanceledView(generic.TemplateView):
    template_name = "checkout/canceled.html"
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name )

@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {
            'publicKey': settings.STRIPE_PUBLISHABLE_KEY,
            'basePrice': 123,
            'currency': "JPY",
        }
        return JsonResponse(stripe_config, safe=False)

@csrf_exempt
def onetime_payment_checkout(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        domain_url = "http://localhost:8080/"#os.getenv('DOMAIN')
        stripe.api_key = settings.STRIPE_SECRET_KEY
        try:
            # Create new Checkout Session for the order
            # Other optional params include:
            # [billing_address_collection] - to display billing address details on the page
            # [customer] - if you have an existing Stripe Customer ID
            # [payment_intent_data] - lets capture the payment later
            # [customer_email] - lets you prefill the email input in the form
            # For full details see https:#stripe.com/docs/api/checkout/sessions/create

            # ?session_id={CHECKOUT_SESSION_ID} means the redirect will have the session ID set as a query param
            checkout_session = stripe.checkout.Session.create(
                success_url=domain_url +
                "checkout/success?session_id={CHECKOUT_SESSION_ID}",
                cancel_url=domain_url + "checkout/canceled/",
                payment_method_types=["card"],
                line_items=[
                    {
                        "name": "Pasha photo",
                        "images": ["https://picsum.photos/300/300?random=4"],
                        "quantity": data['quantity'],
                        "currency": "JPY",
                        "amount":365, #os.getenv('BASE_PRICE'),
                    }
                ]
            )
            logger.debug( str(checkout_session))
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            logger.warning( str(e) )
            return JsonResponse({'error':str(e)})
