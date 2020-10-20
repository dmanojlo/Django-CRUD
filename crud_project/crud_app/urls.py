"""crud_project URL Configuration

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
from django.conf.urls import url, include
from my_crud_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^izdano/$', views.IndexView.as_view(), name='index'),
    url(r'^ajax/izdano_edit/(?P<pk>\d+)/$', views.izdano_edit, name='izdano_edit'),
    url(r'^ajax/izdano_delete/(?P<pk>\d+)/$', views.izdano_delete, name='izdano_delete'),
    #path('edit/<int:pk>/', views.edit, name='edit'),
    #path('create/', views.create, name='create'),
    url(r'^ajax/izdano_create_edit/$', views.izdano_create_edit, name='izdano_create_edit'),
    url(r'^search_res/$', views.filter_view, name='filter_view'),
    #path('ajax/status/',  views.status, name='status'),
    url(r'^ajax/status/$', views.status, name='status'),
    #path('delete/<int:pk>/', views.delete, name='delete'),
]
