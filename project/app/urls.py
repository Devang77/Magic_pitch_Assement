from django.urls import path
from .views import *
from .Auth import *
urlpatterns = [
    path('registration',registration,name='registration'),
    path('user_detail',user_detail,name='user_detail'),
    path('referals',referals,name='referals')
]