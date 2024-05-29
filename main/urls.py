from django.urls import path
from . import views

urlpatterns = [
    path('catalog/', views.phone_catalog, name='phone_catalog'),
    path('catalog/<slug:slug>/', views.phone_detail, name='phone_detail'),
]
