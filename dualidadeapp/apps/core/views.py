from django.shortcuts import render
from demands.views import list_demands

# Create your views here.

def home(request):
    template_name ='core/home.html'
    context = {}
    return render(request, template_name, context)