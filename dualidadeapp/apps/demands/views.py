from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .forms import DemandForm
from .models import Demand

# Create your views here.

def add_demand(request):
    template_name = 'demands/add_demand.html'
    context = {}
    if request.method == 'POST':
        form = DemandForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('demands:list_demands')
    form = DemandForm()
    context['form'] = form
    return render(request, template_name, context)

def list_demands(request):
    template_name = 'demands/list_demands.html'
    demands = Demand.objects.filter()
    context = {
        'demands': demands
    }
    return render(request, template_name, context)

def edit_demand(request, id_demand):
    template_name = 'demands/add_demand.html'
    context ={}
    client = get_object_or_404(Demand, id=id_demand)
    if request.method == 'POST':
        form = DemandForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('demands:list_demands')
    form = DemandForm(instance=client)
    context['form'] = form
    return render(request, template_name, context)

def delete_demand(request, id_demand):
    demand = Demand.objects.get(id=id_demand)
    demand.delete()
    return redirect('demands:list_demands')

def search_demands(request):
    template_name = 'demands/list_demands.html'
    query = request.GET.get('query')
    demands = Demand.objects.filter(title__icontains=query)
    context = {
        'demands': demands
    }
    return render(request,template_name, context)