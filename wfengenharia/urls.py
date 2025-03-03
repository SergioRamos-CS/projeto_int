from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.home, name='home'),
    
    path('clientes/', views.clientes, name='clientes'),
    path('clientes/add/', views.add_cliente, name='add_cliente'),
    path('clientes/edit/<int:id_cliente>/', views.edit_cliente, name='edit_cliente'),
    path('clientes/delete/<int:id_cliente>/', views.delete_cliente, name='delete_cliente'),
    
    path('obras/', views.obras, name='obras'),
    path('obras/add/', views.add_obra, name='add_obra'),
    path('obras/edit/<int:id_obra>/', views.edit_obra, name='edit_obra'),
    path('obras/delete/<int:id_obra>/', views.delete_obra, name='delete_obra'),
]