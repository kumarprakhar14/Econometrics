from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login, logout
from webApp.models import Contact
from django.contrib import messages
from datetime import datetime
from joblib import load

# users
# 1. admin(admin)
# 2. kumar.prakhar(kprakhar@12345)

model = load("Models\\elastic_net.joblib")

def predict(request):

    result = None
    if request.method == 'POST':
        landAgric = float(request.POST.get('landAgric'))
        urbanBuildup = float(request.POST.get('urbanBuildup'))
        GDPagric = float(request.POST.get('GDPagric'))
        GDPindus = float(request.POST.get('GDPindus'))
        GDPser = float(request.POST.get('GDPser'))

        result = model.predict([[landAgric, urbanBuildup, GDPagric, GDPindus, GDPser]])
        print(result)
    return render(request, 'results.html', {'result':result})


# Create your views here.
def index(request):
    # check if user is logged in
   if request.user.is_anonymous:
       return redirect("/login")
   return render(request, 'index.html')

def loginUser(request):
    if request.method == 'POST':
   # check if user has entered correct credentials
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect("/")
        else:
            # No backend authenticated the credentials
            return render(request, 'login.html')
    else: 
        return render(request, 'login.html', {'error': 'Invalid username or password'})
    
def logoutUser(request):
   logout(request)
   return redirect("/login")
    
def totalGDP(request):
    return render(request, 'totalGDP.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today()) 
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'contact.html')

def pricing(request):
    return render(request, 'pricing.html')

def about(request):
    return render(request, 'aboutus.html')

def services(request):
    return render(request, 'services.html')