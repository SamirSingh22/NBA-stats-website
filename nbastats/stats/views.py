from django.shortcuts import render
from django.http import HttpResponse
from .models import Player, Team
from . import stat_getter

def stats(request):
	return render(request, 'stats/stat_home.html')

def player_list(request):
	players = Player.objects.all().order_by('last_name')
	return render(request, 'stats/list_player.html', {'players': players})

def career_stats(request, slug, per_mode):
	modes = ['Per Game', 'Totals']
	modes_link = ['PerGame', 'Totals']
	player = Player.objects.get(slug=slug)
	stats_h, stats_b = stat_getter.career_stats(player.player_id, per_mode)
	ndx = 0
	if per_mode == modes_link[1]:
		ndx = 1
		other = 0
	else:
		other = 1
	return render(request, 'stats/player_stats.html', {'player': player, 'headers': stats_h, 'stats': stats_b,
													   'per_mode': modes[ndx], 'other_mode_link': modes_link[other],
													   'other_mode_name': modes_link[other]})

def team_list(request):
	return render(request, 'stats/list_team.html')

def player_profile(request, slug):
	player = Player.objects.get(slug=slug)
	return render(request, 'stats/player_profile.html', {'player': player})

def team_profile(request, slug):
	team = Team.objects.get(slug=slug)
	return render(request, 'stats/team_profile.html', {'team': team})

# Create your views here.
