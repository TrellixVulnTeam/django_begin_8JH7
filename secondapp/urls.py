"""firstapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
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
from . import views
from django.urls import path

urlpatterns = [
    path('main/', views.main),
    path('insert/', views.insert),
    path('show/', views.show),
    path('insertCourse/', views.insertCourse),
    path('showCourse/', views.showCourse),
    path('armyShop/', views.armyShop),
    # path parameter
    # path('armyShop/<int:year>/<int:month>', views.army_shop_path),
    # Query Parameter
    path('armyShop_query/', views.army_shop_query),
    path('req/ajax/get', views.ajax_get),
    path('req/ajax/exam', views.ajax_Exam),
]
