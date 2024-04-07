from django.shortcuts import render,redirect
from datetime import datetime,timedelta,time,date
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Count,Sum,Case,When,F,Q
from rest_framework.exceptions import *
from django.db import connection
# from .apr_views import *
from rest_framework.exceptions import AuthenticationFailed
from jwt.exceptions import *
from rest_framework.exceptions import *
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import json
import jwt
import random
import os



secret_key="7qOTUbxGfmX77siMGePH"

def verify_token(view_func):
    def _wrap_view(request,*args,**kwargs):
        print(type(request))
        token=request.session.get('Authorization')
        print(token,'ooooooooooooooooooooo')
        if not token:
            print('hiiiiiiii')
            raise AuthenticationFailed("No Authentication token")
        try:
            token=token
            # print(token,'kkkkkkkkkkkkkkkkkkkkkkkkkkkkk')
            check_token=Valid_token.objects.get(token=token)
            print(check_token)
            if check_token and check_token.token==token:
                print('hiiiiiiiiiiiiiiii')
                payload=jwt.decode(token,secret_key,algorithms=["HS256"])
            else:
                raise AuthenticationFailed("Token Not valid")
        # except jwt.ExpiredSignatureError:
        #     raise exceptions.AuthenticationFailed("Token Has Expired")
        # except jwt.DecodeError:
        #     raise exceptions.AuthenticationFailed("Invalid authentication token")
        except Valid_token.DoesNotExist:
            raise AuthenticationFailed("Enter Valid token")
        request.jwt_payload=payload
        return view_func(request,*args,**kwargs)
    return _wrap_view

