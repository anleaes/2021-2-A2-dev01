from django.urls import path
from . import views
from demands.views import list_demands

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
]
