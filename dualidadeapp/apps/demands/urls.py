from django.urls import path
from . import views

app_name = 'demands'

urlpatterns = [
    path('', views.list_demands, name='list_demands'),
    path('adicionar/', views.add_demand, name='add_demand'),
    path('editar/<int:id_demand>/', views.edit_demand, name='edit_demand'),
    path('excluir/<int:id_demand>/', views.delete_demand, name='delete_demand'),
    path('buscar/', views.search_demands, name='search_demands'),

]