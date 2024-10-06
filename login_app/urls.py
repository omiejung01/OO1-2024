from django.urls import path
from . import views

urlpatterns = [

    path('', views.homepage, name='homepage'),
    #path('user_list', views.user_list, name='user_list'),
    path('login', views.login, name='login'),

]