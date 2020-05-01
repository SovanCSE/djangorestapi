"""djangorestapi URL Configuration

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
from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

route1 = DefaultRouter()
route1.register('student', StudentViewSet, basename='student')

route2 = DefaultRouter()
route2.register('student',StudentGenericViewSet, basename='student')

route3 = DefaultRouter()
route3.register('student',StudentModelViewSet, basename='student')

urlpatterns = [

    #Wokring with functional based api ==>
    # path('student/', studet_list, name='student_list'),
    # path('student/<int:pk>/', student_detail, name='student_detail')

    #Working with functional base api View using api_view decorator ==>
    # path('student/', studet_list_v2, name='student_list'),
    # path('student/<int:pk>/', student_detail_v2, name='student_detail')

    #Working with class base api view using APIView in restframework class==>
    # path('student/', StudetListAPIView.as_view(), name='student_list'),
    # path('student/<int:pk>/', StudentDetailAPIView.as_view(), name='student_detail')

    #Wokring with class base api view using Genericview and mixins restframework classes:==>
    # path('student/', StudentListGenericAPIView.as_view(), name='student_list'),
    # path('student/<int:id>/', StudentDetailGenericAPIView.as_view(), name='student_detail')

    #working with class based rest api view using Viewset & Router restframework classes:==>
     # path('', include(route1.urls), name='student_list'),
     # path('<int:pk>/', include(route1.urls), name='student_detail')

    # working with class based rest api view using GenericViewset & Router restframework
    # classes:==>
    # path('', include(route2.urls), name='student_list'),
    # path('<int:pk>/', include(route2.urls), name='student_detail')

   # working with class based rest api view using ModelViewset & Router restframework
    # classes:==>
    path('', include(route3.urls), name='student_list'),
    path('<int:pk>/', include(route3.urls), name='student_detail')

]
