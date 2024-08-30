from django.shortcuts import render,redirect
from django.contrib.auth.models import User
# from django.contrib.auth.hashers import make_password
from . forms import SignupForm,LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login



# from django.template import loader
def index(request):
    return render(request,'index.html')
def login_page(request):
    if request.method == 'POST':       
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']   
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful.')
                return redirect('search_page')
            else:
                # Display an error message if authentication fails
                messages.error(request, 'Invalid username or password. Please try again.')
        else:
            # Display an error message if the form is invalid
            messages.error(request, 'Invalid form submission. Please check your input.')        
    else:
        form = LoginForm()
    return render(request, 'login_page.html', {'form': form})

def register_page(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User(username=username, email=email)
            user.set_password(password)
            user.save()
            messages.success(request, 'Registration successful. You can now log in.')
            return redirect('login_page')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = SignupForm()
    return render(request, 'register_page.html', {'form': form})

                    
def search_page(request):
    messages.info(request, 'You are now on the search page.')
    return render(request, 'search_page.html')

# Create your views here.
