# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import JsonResponse
import urllib2
import random
import json
from LoginRegister.models import UserDetail
from django.contrib.auth.models import User
# Create your views here.
@csrf_exempt
def verifyOtp(request):
	if request.method == "POST":
		username = request.POST.get('username')
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        gender = request.POST.get('gender')
        password = request.POST.get('password')

        otp = request.POST.get("otp")


        authKey = "176332A81pH4L759c8aad6"

        print(mobile)

        verifyOtpUrl = "https://control.msg91.com/api/verifyRequestOTP.php?authkey="+authKey+"&mobile=91"+str(mobile)+"&otp="+str(otp)+""

        response = urllib2.urlopen(verifyOtpUrl).read()

        response = json.loads(response)
        print(response)	



        if response['type'] == 'success':
			data = {
				"success" : True,
				"message" : "User Verified"
			}

			userDetailObj = UserDetail.objects.create(
                name=name,
                mobile=mobile,
                gender=gender,
                username=username
            )


			userObj = User.objects.create_user(username=username,password=password)

        else:
	
			data = {
				"success" : False,
				"message" : "Number verification failed"
			} 	

        return JsonResponse(data,safe=False)