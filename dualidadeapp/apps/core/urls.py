from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.list_demands, name='list_demands'),
]
