from django.urls import path
from . import views

urlpatterns = [
   path('', views.main_view), 
   path('cart/', views.cart_view, name='cart'), 
]
