
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User



from django.contrib.auth.models import User
from django.contrib import messages

def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # Check if username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists. Please choose another.')
            return redirect('signup')
        
        user = User.objects.create_user(username=username, password=password)
        user.save()
        messages.success(request, 'Account created successfully. Please log in.')
        return redirect('login')
    
    return render(request, 'accounts/signup.html')



# Login View
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html', {'error': 'Invalid username or password'})
    return render(request, 'accounts/login.html')



@login_required(login_url='login')
def cart_view(request):
    # Logic for displaying the cart items
    return render(request, '/cart.html')

@login_required
def profile_view(request):
    return render(request, 'accounts/profile.html')


# Logout View
def logout_view(request):
    logout(request)
    return redirect('home')

from django.shortcuts import render, redirect
from .forms import ProfileForm
from .models import Profile

def profile_view(request):
    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'accounts/profile.html', {'form': form, 'profile': profile})
