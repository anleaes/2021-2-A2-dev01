from django.shortcuts import render, get_object_or_404, redirect
from .forms import TeamForm
from .models import Team, User, TeamUser

# Create your views here.

def add_team(request):
    template_name = 'teams/add_team.html'
    context = {}
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('teams:list_teams')
    form = TeamForm()
    context['form'] = form
    return render(request, template_name, context)

def list_teams(request):
    template_name = 'teams/list_teams.html'
    team_users = TeamUser.objects.filter()
    users = User.objects.filter()
    teams = Team.objects.filter()
    context = {
        'teams': teams,
        'users': users,
        'team_users': team_users
    }
    return render(request, template_name, context)

def edit_team(request, id_team):
    template_name = 'teams/add_team.html'
    context ={}
    team = get_object_or_404(Team, id=id_team)
    if request.method == 'POST':
        form = TeamForm(request.POST, instance=team)
        if form.is_valid():
            form.save()
            return redirect('teams:list_teams')
    form = TeamForm(instance=team)
    context['form'] = form
    return render(request, template_name, context)

def delete_team(request, id_team):
    team = Team.objects.get(id=id_team)
    team.delete()
    return redirect('teams:list_teams')