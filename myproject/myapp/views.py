from django.shortcuts import render
# from django.template import loader
def index(request):
    return render(request,'index.html')
def login_page(request):
    return render (request,'login_page.html')
def register_page(request):
    return render(request,'register_page.html')
def search_page(request):
    return render(request,'search_page.html')

# Create your views here.
