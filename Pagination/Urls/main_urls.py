"""newdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path,re_path,include
from app01 import views
import pro
from pro import urls

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    # path('chen/<int:year>/<str:num>', views.home),
    path('home/', views.home),
    re_path(r'page/$',views.page),
    re_path(r'^stu_from/$',views.stufrom),
    re_path(r'^stu_model_from/$',views.stumodelfrom),
    re_path(r'^pro/',include('pro.urls')),
    # path('',pro.views.index),
    path('accounts/login/',pro.views.userlogin),
    path('accounts/logout/',pro.views.userlogout),
]
