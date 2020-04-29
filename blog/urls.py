"""Django_Blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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
from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('links/', views.links, name='links'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('tag/<int:id>/', views.tag_detail, name='tag'),
    path('article/<int:id>/', views.article_detail, name='article'),
    path('category/<slug>/', views.category_detail, name='category'),
    path('search/', views.search, name='search'),
    path('error/<errmsg>/', views.error, name='error'),
]
