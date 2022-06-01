from django.urls import path
from . import views

urlpatterns = [
   path('', views.main_view), 
   path('products/', views.products_view, name='products'), 
   path('categories/', views.categories_view, name='categories'), 
   path('vendors/', views.vendors_view, name='vendors'),
   path('buy/', views.buy_view, name='buy'), 
]
