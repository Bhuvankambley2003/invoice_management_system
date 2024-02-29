"""
URL configuration for dbms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import include, path
from mini import views

app_name = 'mini'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('invoice-list/', views.invoice_list, name='invoice_list'),
    path('add-invoice/', views.add_invoice, name='add_invoice'),
    path('edit-invoice/<int:invoice_id>/', views.edit_invoice, name='edit_invoice'),
    path('delete-invoice/<int:invoice_id>/', views.delete_invoice, name='delete_invoice'),
   
    
]


