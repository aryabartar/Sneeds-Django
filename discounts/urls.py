"""sneeds URL Configuration

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
from django.urls import path
from . import views

app_name = "cafe"
urlpatterns = [
    path('discounts/', views.DiscountList.as_view(), name="discount_list"),
    path('discounts/<int:discount_pk>', views.DiscountDetail.as_view(), name="discount_detail"),
    path('user-discounts/', views.UserDiscountList.as_view(), name="user_discount_list"),
    path('user-discounts/<int:user_discount_pk>', views.UserDiscountDetail.as_view(), name="user_discount_detail"),
    # path('user-discounts-archive/', views.UserDiscountArchiveList.as_view(),
    #      name="user_discount_archive_list"),
    path('cafes/', views.CafeList.as_view(), name="cafe_list"),
    path('cafes/<str:cafe_slug>/', views.CafePage.as_view(), name="cafe_detail"),
    path('cafes/<str:cafe_slug>/discounts', views.CafeDiscountsPage.as_view(), name="cafe_discounts_list"),
]
