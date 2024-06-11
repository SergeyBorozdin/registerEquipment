from django.urls import path
from . import views

urlpatterns = [
    path('', views.equipment_list, name='equipment_list'),
    path('equipment/<int:pk>/', views.equipment_detail, name='equipment_detail'),
    path('equipment/new/', views.equipment_new, name='equipment_new'),
    path('equipment/<int:pk>/edit/', views.equipment_edit, name='equipment_edit'),
]
