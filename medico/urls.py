from django.urls import path
from .import views

urlpatterns = [
    path('', views.lista_medicos, name='lista-medicos'),
    path('detalhe/<int:pk>/', views.medico_detalhe, name='medico_detalhe'),
]
