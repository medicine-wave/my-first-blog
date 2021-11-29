from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),

    path('register/', views.registerPage, name = 'register'),
    path('login/', views.loginPage, name = "login"),
    path('logout/', views.logoutUser, name = "logout"),

    path('home/', views.home, name = "home"),
    ]
