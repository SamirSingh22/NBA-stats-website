from django.shortcuts import render
from django.http import HttpResponse
from .models import Player
from . import stat_getter

def stats(request):
	return render(request, 'stats/stat_home.html')

def player_list(request):
	players = Player.objects.all().order_by('last_name')
	return render(request, 'stats/list_player.html', {'players': players})

def career_stats(request, slug, per_mode):
	modes = ['Per Game', 'Totals']
	player = Player.objects.get(slug=slug)
	stats_h, stats_b = stat_getter.career_stats(player.player_id, per_mode)
	if per_mode == 'PerGame':
		other_mode_link = 'Totals'
		other_mode_name = 'Totals'
	else:
		other_mode_link = 'PerGame'
		other_mode_name = 'Per Game'
	return render(request, 'stats/player_stats.html', {'player': player, 'headers': stats_h, 'stats': stats_b,
													   'per_mode': per_mode, 'other_mode_link': other_mode_link,
													   'other_mode_name': other_mode_name})

def team_list(request):
	return render(request, 'stats/list_team.html')

def player_profile(request, slug):
	player = Player.objects.get(slug=slug)
	return render(request, 'stats/player_profile.html', {'player': player})

# Create your views here.
