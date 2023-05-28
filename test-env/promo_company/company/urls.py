from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

from camp import views
urlpatterns = [

    path('yp_company', views.yp_company, name='yp_company'),
    path('create_company', views.create_company, name='create_company'),
    path('my_company', views.my_company, name ='my_company'),
    path('company/<int:id_campaign>', views.show_company, name='show_company'),
    path('edit_company/<int:id_campaign>', views.edit_company, name='edit_company'),
    path('edit_home/<int:id_campaign>', views.edit_home, name='edit_home'),
    path('poll_edit/<int:id_campaign>', views.poll_edit, name='poll_edit'),
    path('poll_form/<int:id_campaign>', views.poll, name='poll'),
    path('poll_info/<int:id_poll>', views.poll_info, name='poll_info'),
    path('poll_form/<int:id_form>', views.poll_form, name='poll_form')
]