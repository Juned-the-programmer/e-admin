from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('dashboard',views.dashboard,name='dashboard'),
    path('orders',views.order,name="orders"),
    path('subcategory',views.nothing,name='nothing'),
]

