from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [


    path('login', auth_views.LoginView.as_view(template_name='login.html'), name ='log'),
    path('user_page', views.user_page, name="user_page"),
    path('no', views.no, name="no"),
    path('reg', views.reg, name="reg"),
    path('yep', views.yep, name= 'yep'),
]