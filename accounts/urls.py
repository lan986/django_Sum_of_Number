
from django.urls import path
from . import views

urlpatterns = [
 
        path('registers',views.registers,name='registers'),
        path('login',views.login,name='login')
]