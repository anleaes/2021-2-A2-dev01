from django.shortcuts import render, get_object_or_404, redirect
from demands.forms import DemandForm
from demands.models import Demand

# Create your views here.


def list_demands(request):
    template_name = 'demands/list_demands.html'
    demands = Demand.objects.filter()
    context = {
        'demands': demands
    }
    return render(request, template_name, context)