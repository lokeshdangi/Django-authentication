from django.urls import path,include
from django.conf.urls import url

from . import views

app_name = 'account'


urlpatterns = [
        url(r'^$', views.login, name='login'),
        url(r'^login/$', views.login, name='login'),
        url(r'^signup/$', views.signup, name='signup'),
        url(r'^logout/$', views.logout, name='logout'),
        url(r'^reset_password/$', views.reset_password, name='reset_password'),
    
    ]
