from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from . forms import SignupForm

# from django.template import loader
def index(request):
    return render(request,'index.html')
def login_page(request):
    return render (request,'login_page.html')
def register_page(request):
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            user=User(username=username,email=email)
            user.set_password(password)
            user.save()
            return redirect('login_page')
    else:
        form=SignupForm()
    return render(request,'register_page.html',{'form':form})
                    
def search_page(request):
    return render(request,'search_page.html')

# Create your views here.
