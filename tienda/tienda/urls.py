

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from online import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('pedido/', views.pedido, name='pedido'),
    path('producto/<int:id>/', views.detalle_producto, name='detalle_producto'),
    path('seguimiento/', views.seguimiento, name='seguimiento'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

