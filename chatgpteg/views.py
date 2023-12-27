
from django.contrib.auth import authenticate, login
from .forms import RegistrationForm, LoginForm
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth import logout
from django.shortcuts import redirect

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Process registration logic here (create user, save to database)
            return redirect('login')
    else:
        form = RegistrationForm()

    return render(request, 'chatgpteg/register.html', {'form': form})



def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                # Redirect to a dashboard or home page
                return redirect('dashboard')
    else:
        form = LoginForm()

    return render(request, 'chatgpteg/login.html', {'form': form})



def logout_user(request):
    logout(request)
    # Redirect to the login page or home page
    return redirect('login')


