"""project_zaiko URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from inventario import views as inventarioViews
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inventarioViews.home, name="inicio"),
    path('inventario/',inventarioViews.inv, name="inventario"),
    path('crear/',inventarioViews.crearProducto, name="crear"), 
    path('editar/<pk>/',inventarioViews.actualizarProducto, name="editar"),    
    path('vender/<pk>/',inventarioViews.venderProducto, name="vender"),  
]


urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)