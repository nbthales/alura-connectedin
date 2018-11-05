from django.urls import path
from perfis import views

urlpatterns = [
    path('', views.index, name='index'),
    path('perfis/<perfil_id>', views.exibir, name='exibir'),
    path('perfis/<perfil_id>/convidar', views.convidar, name='convidar'),
    path('convite/<convite_id>/aceitar', views.aceitar, name='aceitar')
]
