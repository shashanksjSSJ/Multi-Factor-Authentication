from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import login, authenticate
from .models import CustomUser
from django.contrib import  messages
import requests
import json
from django.core.mail import send_mail

from django.contrib.auth.decorators import login_required

import random

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # Redirect to a success page, or you can customize this as needed
            return redirect('otp_pin')
        else:
            messages.error(request, 'Invalid username or password. Please try again.')

    return render(request, 'login.html')


@login_required
def otp_pin_view(request):
    user = request.user
    user_pin = user.pin
    user_phone_number = user.phone_number
    message = f"Hello, {user.username}! Someone is trying to access your account, please ignore the message if it is you"
    send_mail(
                "Someone is trying to login",
                message,
                ' ',  # Sender's email address
                [user.email],  # List of recipient email addresses
                fail_silently=False,
            )
    message1 = ""
    if request.method == 'POST':
        entered_otp = request.POST.get('otp')
        stored_otp = request.session.get('otp')
        pin = request.POST.get('pin')
        if entered_otp == stored_otp and pin == user_pin:
            print("Worked")
            messages.success(request, 'OTP and pin verification successful!')
            send_mail(
                "Login Successful",
                f"Hello {user.username}, You have logged in successfully!!",
                ' ',  # Sender's email address
                [user.email],  # List of recipient email addresses
                fail_silently=False,
            )
            del request.session['otp']
            return redirect('success') 
        else:
            print('wrong')
            send_mail(
                "Unsuccessful Login",
                f"Hello {user.username}, Someone tried to enter and wrong OTP or password has been entered!!",
                ' ',  # Sender's email address
                [user.email],  # List of recipient email addresses
                fail_silently=False,
            )
            message1 = "Wrong OTP or Password"
            messages.error(request, 'Invalid OTP or pin. Please try again.')

    
    otp = ''.join(random.choices('0123456789', k=6))

    send_otp_via_textbelt(user_phone_number, otp)
    
    request.session['otp'] = otp
    print("YESSSS!!!!!")
   
    return render(request, 'otp.html', {'otp': otp, 'message':message1})



def send_otp_via_textbelt(phone_number, message):
    otp_service_url = ' '  # Update with the actual URL

    data = {
        "to": phone_number,
        "message": message
    }

    # Make sure the Content-Type header is set appropriately based on the data format
    headers = {
        'Authorization': ' ',
    }

    # Ensure you are using the correct HTTP method (POST)
    response = requests.post(otp_service_url, json=data, headers=headers)

    print("Response Details:")
    print("Status Code:", response.status_code)
    print("Headers:", response.headers)
    print("Content:", response.text)



def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            send_mail(
                "Welcome to 3 Factor Authentication",
                "Welcome!! You have newly registered!!",
                ' ',  # Sender's email address
                [user.email],  # List of recipient email addresses
                fail_silently=False,
            )
            print("working")
            login(request, user)
            return redirect('login')  
        else: 
            print(form.errors)
    else:
        form = CustomUserCreationForm()

    return render(request, 'register.html', {'form': form})


@login_required
def success(request):
    return render(request,'success.html')