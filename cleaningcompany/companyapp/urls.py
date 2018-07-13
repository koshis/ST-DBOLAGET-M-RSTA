from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.home,name ="home"), 
    url(r'^quality/$', views.quality, name='quality'),
    url(r'^cleaning/$', views.cleaning, name='cleaning'),
    url(r'^propertyservice/$', views.propertyservice, name='propertyservice'),
    url(r'^category/(?P<title>[^/]+)/$', views.pages,name ="pages"),
    url(r'^$', views.valid_form, name ="valid-form"), 

    





]
