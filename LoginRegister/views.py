# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import JsonResponse
import jwt
import urllib2
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
import random
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from .models import UserDetail
# Create your views here.
def index(request):
    return render(request,'register.html')

@csrf_exempt    
def register(request):
    data = {}
    if request.method == "POST":
        username = request.POST.get('username')
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        gender = request.POST.get('gender')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            data['success'] = False
            data['message'] = "User already registered"

            return JsonResponse(data,safe=False)
        

        else:
            # userDetailObj = UserDetail.objects.create(
            #     name=name,
            #     mobile=mobile,
            #     gender=gender,
            #     username=username
            # )

            # userObj = User.objects.create_user(username=username,password=password)

            authKey = "176332A81pH4L759c8aad6"
            senderId = "MSGMSG"
            otp = random.randint(2000,9999)

            print(otp)

            try:
                sendOtpUrl = "https://control.msg91.com/api/sendotp.php?authkey="+authKey+"&mobile=91"+str(mobile)+"&message=Your%20otp%20is%20"+str(otp)+"&sender="+senderId+"&otp="+str(otp)+""

                response = urllib2.urlopen(sendOtpUrl).read()

                print(response)

            except Exception as e:
                print(str(e))
                data['success'] = False
                data['message'] = "Otp not sent"

                return JsonResponse(data,safe=False)

            data = {}
            data['success'] = True
            data['message'] = "User Registered"

            return JsonResponse(data,safe=False)
     