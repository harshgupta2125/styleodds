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
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

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
    return render(request, 'checkout.html')

def success_view(request):
    return render(request, 'success.html')

def vintage_archive(request):
    return render(request, 'vintage_archive.html')

def style_boards(request):
    return render(request, 'style_boards.html')




from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def user_dashboard(request):
    return render(request, 'dashboard.html')

@login_required(login_url='login')  # redirect to login page if not logged in
def cart(request):
    # your cart logic here
    return render(request, 'cart.html')

@login_required(login_url='login')
def style_boards(request):
    # your style board logic here
    return render(request, 'style_boards.html')



# payment gateway
@csrf_exempt
def create_checkout_session(request):
    if request.method == 'POST':
        stripe.api_key = settings.STRIPE_SECRET_KEY

        try:
            # You can calculate total dynamically from cart
            session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[
                    {
                        'price_data': {
                            'currency': 'inr',
                            'product_data': {
                                'name': 'Clothing Purchase',
                            },
                            'unit_amount': 1000 * 100,  # ₹1000 (multiply by 100 because Stripe uses paise)
                        },
                        'quantity': 1,
                    },
                ],
                mode='payment',
                success_url='http://127.0.0.1:8000/success/',
                cancel_url='http://127.0.0.1:8000/cart/',
            )
            return redirect(session.url, code=303)
        except Exception as e:
            return JsonResponse({'error': str(e)})
    return render(request, 'checkout.html')