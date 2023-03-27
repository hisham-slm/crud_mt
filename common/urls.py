from . import views
from django.urls import path


app_name = 'common'

urlpatterns = [
    path('',views.home,name='home'),
    path('login',views.login,name='login'),
    path('signup',views.signup,name='signup'),
    path('username_exist',views.username_exist,name='username_exist'),
    path('admin/',views.admin_login,name='admin_login'),
]