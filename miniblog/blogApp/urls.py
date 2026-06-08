"""miniblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from blogApp import views

urlpatterns = [
    path('home/', views.home),
    path('get_login/', views.get_login),
    path('post_login/',views.post_login),
    path('logout_user/', views.logout_user),
    path('get_register/',views.get_register),
    path('post_register/',views.post_register),
    path('viewdata/',views.viewdata),
    path('get_changepassword/',views.get_changepassword),
    path('post_changepassword/',views.post_changepassword),
    path('viewprofile/',views.viewprofile),
    path('get_editprofile/',views.get_editprofile),
    path('post_editprofile/',views.post_editprofile),
    path('userhome/', views.userhome),
    path('adminhome/', views.adminhome),
    path('block_user/<int:id>/', views.block_user),
    path('unblock_user/<int:id>/', views.unblock_user),
    path('get_addblog/',views.get_addblog),
    path('post_addblog/', views.post_addblog),
    path('view_myblogs/', views.view_myblogs),
    path('get_editblog/<int:id>/',views.get_editblog),
    path('post_editblog/<int:id>/',views.post_editblog),
    path('delete_blog/<int:id>/',views.delete_blog),
    path('view_allblogs/',views.view_allblogs),
    path('view_blog/<int:id>/', views.view_blog),
    path('view_blog/<int:id>/', views.view_blog),
    path('add_comment/<int:id>/', views.add_comment),
    path('viewallblogs_admin/',views.viewallblogs_admin),
    path('approve_blog/<int:id>/',views.approve_blog),
    path('reject_blog/<int:id>/',views.reject_blog),
    path('delete_blog_admin/<int:id>/', views.delete_blog_admin),
]

