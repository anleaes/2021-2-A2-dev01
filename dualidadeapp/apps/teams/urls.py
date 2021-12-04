from django.urls import path
from . import views

app_name = 'teams'

urlpatterns = [
    path('', views.list_teams, name='list_teams'),
    path('adicionar/', views.add_team, name='add_team'),
    path('editar/<int:id_team>/', views.edit_team, name='edit_team'),
    path('excluir/<int:id_team>/', views.delete_team, name='delete_team'),
]