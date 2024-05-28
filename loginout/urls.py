from django.urls import path
from loginout.views import *

urlpatterns = [
    path('', register, name='register'),
    path('login/', mylogin, name='login'),
    path('logout/', mylogout, name='logout'),
    path('home/', home, name='home')
]