from django.urls import path 
from .views import *


urlpatterns = [
    path('login', login, name="Login"),
    path('x/register', register, name="Register"),
    path('register', registeruser, name="RegisterPage"),
    path('logout', logout, name="Logout"),
    path('contact', contact, name="Contact"),
    path('x/contact', contactform, name="Contact"),
    path('about', about, name="About"),
    path('', root, name="ROOT"),
]