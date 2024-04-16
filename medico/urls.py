from django.urls import path
from . import views

urlpatterns = [
    path('', views.medico_nomeado, name='medico_nomeado'),
    path('medico/<int:pk>/', views.medico_lista, name='medico_detail'),
]
