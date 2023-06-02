"""promo URL Configuration

The 'urlpatterns' list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

from comp import views
from .views import comps



urlpatterns = [
    path(' ', views.comps, name='comps'),
    path('createcomp', views.createcomp, name='createcomp'),
    path('mycomp', views.mycomp, name='mycomp'),
    path('formbupass/<int:id_company>', views.formbupass, name='formbupass'),
    path('comps/<int:id_company>', views.showcomp, name='showcomp'),
    path('editcomp/<int:id_company>', views.editcomp, name='editcomp'),
    path('homeedit/<int:id_company>', views.homeedit, name='homeedit'),
    path('bupassedit/<int:id_company>', views.bupassedit, name='bupassedit'),
    path('showbupass/<int:id_bupass>', views.showbupass, name='showbupass'),
    path('showhome/<int:id_home>', views.showhome, name='showhome'),
    path('showsurveyform/<int:id_form', views.showsurveyform, name='showsurveyform'),
    
]
