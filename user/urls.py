from . import views
from django.urls import path


app_name = 'user'

urlpatterns = [
    path('',views.home,name='user_home'),
    path('create_post',views.create_post,name='create_post'),
    path('uploaded_post',views.uploaded_post,name='uploaded_post'),
    path('like_post/<int:pid>',views.like_post,name='like_post'),
    path('logout',views.logout,name='logout'),
]