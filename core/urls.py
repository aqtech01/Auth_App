from django.urls import path
from core.views import *

urlpatterns = [
    path("",login_page,name="login_page"),
    path("signup/",signup_page,name="signup_page"),
    path("home/",home,name="home"),
    path("logout/",logout_page,name="logout"),
    
    
]
