from app_admin import views
from django.urls import path


app_name = 'admin'

urlpatterns = [
    path('home/',views.home,name='home'),
    path('logout/',views.logout,name='logout'),
    path('approve/<int:pid>',views.approve,name='approve'),
    path('reject/<int:pid>',views.reject,name='reject'),
]