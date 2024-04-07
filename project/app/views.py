from django.shortcuts import render
from .models import *
from .Auth import *
from django.http import JsonResponse
import bcrypt
import jwt
# Create your views here.
def registration(request):
    if request.method == "POST":
       
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        referal_code=request.POST.get('referal_code')
        pass_byte=password.encode('utf-8')
        salt=bcrypt.gensalt()
        hash_password=bcrypt.hashpw(pass_byte,salt)
        request.session['Name'] = name
        user_hash_password=hash_password.decode('utf-8')
        user_referal_code= name+'_'+'referal'
        secret_key="7qOTUbxGfmX77siMGePH"
        current_date=datetime.now().date()
        end_day=datetime.combine(current_date,datetime.max.time())
        if referal_code is None:
            print('inside')
            User.objects.create(username=name,email=email,password=user_hash_password,referal_code=user_referal_code)
            payload={
                'username':name,
                'iat':datetime.utcnow(),
                'exp':end_day
            }
            print(payload)
            token = jwt.encode(payload, secret_key, algorithm='HS256')
            Valid_token.objects.filter(userid=name).delete()
            Valid_token.objects.create(token=token, userid=name)
            request.session['Authorization'] = token
            # return response
            return JsonResponse({'message':f'{name} you have registered successfully and your referal code is {user_referal_code} make use of this referal code to earn points'})
        if referal_code != None:
            print(name,email,password,user_referal_code)
            User.objects.create(username=name,email=email,password=user_hash_password,referal_code=user_referal_code,referal_code_used=referal_code)
            
            payload={
                'username':name,
                'iat':datetime.utcnow(),
                'exp':end_day
            }
            print(payload)
            token = jwt.encode(payload, secret_key, algorithm='HS256')
            Valid_token.objects.filter(userid=name).delete()
            Valid_token.objects.create(token=token, userid=name)
            request.session['Authorization'] = token
            # response=JsonResponse({'status':200,'token':token})
            obj=User.objects.filter(referal_code=referal_code).values()
           
            points=obj[0]['points']
            new_points=points+1
            User.objects.filter(referal_code=referal_code).update(points=new_points)
            return JsonResponse({'message':f'{name} registered successfully by using The {referal_code} code'})
    return JsonResponse({'message':'GET Method not allowed'})  
@verify_token  
def user_detail(request):
    if request.method=="GET":
        userdetail=User.objects.all().values('username','email','referal_code','date_joined')
        return JsonResponse({'message':list(userdetail)})
    return JsonResponse({'message':"Only GET Method Allowed"})
@verify_token
def referals(request):
    if request.method == "GET":
        name=request.session.get('Name')
        print(name)
        current_user=User.objects.filter(username=name).values('referal_code')
        print(current_user[0]['referal_code'])
        current_user_referal_used=User.objects.filter(referal_code_used=current_user[0]['referal_code']).values('username','date_joined')
        return JsonResponse({f'list of user that used {current_user[0]["referal_code"]} code':list(current_user_referal_used)})
