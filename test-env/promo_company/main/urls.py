from django.urls import path, include
from . import views

urlpatterns = [
path ('title',views.title, name = 'title page'),
path ('user', views.user, name = 'user'),
path ('project', views.project, name = 'project')
]
