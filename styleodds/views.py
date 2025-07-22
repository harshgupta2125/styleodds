import json
from django.http import JsonResponse
import stripe
from django.conf import settings
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_protect, ensure_csrf_cookie
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.conf import settings
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY


def home (request):
    return render(request, 'home.html')

def shop (request):
    return render(request, 'shop.html')

def view_details (request):
    return render(request, 'view_details.html')

def cart (request):
    return render(request, 'cart.html')

def about (request):
    return render(request, 'about.html')

def checkout (request):
    return render(request, 'checkout.html', {'STRIPE_PUBLISHABLE_KEY': settings.STRIPE_PUBLISHABLE_KEY})

def success_view(request):
    return render(request, 'success.html')

def vintage_archive(request):
    return render(request, 'vintage_archive.html')

def base(request):
    return render(request, 'base.html')




from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def user_dashboard(request):
    return render(request, 'dashboard.html')

@login_required(login_url='login')  # redirect to login page if not logged in
def cart(request):
    # your cart logic here
    return render(request, 'cart.html')





# payment gateway
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

@csrf_exempt
def create_checkout_session(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON received'}, status=400)

        amount = int(float(data.get('amount', 1000)) * 100)  # convert to paise
        product_name = data.get('product', 'Clothing Purchase')

        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'inr',
                    'product_data': {
                        'name': product_name,
                    },
                    'unit_amount': amount,
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url='https://styleodds.onrender.com/success/',
            cancel_url='https://styleodds.onrender.com/cancel/',
        )
        return JsonResponse({'id': session.id})

