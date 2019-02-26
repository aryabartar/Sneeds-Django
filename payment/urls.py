from django.urls import path, include

from . import views

urlpatterns = [
    path('request/', views.RequestPage.as_view(), name='request'),
    path('verify/', views.verify, name='verify'),
]
