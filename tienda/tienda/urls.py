
from django.contrib import admin
from django.urls import path

from online import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('pedido/', views.pedido),
]
