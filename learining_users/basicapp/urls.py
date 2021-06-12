from django.urls import path 
from basicapp import views
from django.contrib.auth import views as auth_views

app_name = 'basicapp'

urlpatterns = [
    path('registeration/',views.registration,name='registration'),
    path('user_login/',views.user_login,name='user_login'),
]
