from django.shortcuts import render
from .models import *

def home(Request):
    return render(Request,'home.html')

def aboutPage(Request):
    return render(Request,'about.html')

def loanServicePage(Request):
    return render(Request,'loan-services.html')

def applyPage(Request):
    if Request.method=="POST":
        user=loanRequest()
        user.first_name=Request.POST.get('first_name')
        user.last_name=Request.POST.get('last_name')
        user.employment=Request.POST.get('employment')
        user.company_name=Request.POST.get('company_name')
        user.email=Request.POST.get('email')
        user.phone=Request.POST.get('phone')
        user.salary=Request.POST.get('salary')
        user.loan_type=Request.POST.get('loan_type')
        user.aadhar_card=Request.POST.get('aadhar_card')
        user.pan_card=Request.POST.get('pan_card')
        user.salary_sleep=Request.POST.get('salary_sleep')
        user.photo=Request.POST.get('photo')
        
        user.save()
    return render(Request,'apply-now.html')

def contactPage(Request):
    if Request.method=="POST":
        first_name=Request.POST.get('first_name')
        last_name=Request.POST.get('last_name')
        phone=Request.POST.get('phone')
        email=Request.POST.get('email')
        description=Request.POST.get('description')
        user=contact(first_name=first_name,last_name=last_name,phone=phone,email=email,description=description)
        user.save()
    return render(Request,'contact-us.html')

