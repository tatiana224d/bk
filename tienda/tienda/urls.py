

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from online import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('pedido/', views.pedido),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

