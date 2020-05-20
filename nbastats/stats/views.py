from django.shortcuts import render
from django.http import HttpResponse
from .models import Player
from nba_api.stats.static import players
from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.library.parameters import SeasonType


def player_list(request):
	players = Player.objects.all().order_by('last_name')
	return render(request, 'stats/list_player.html', {'players': players})


def player_stats(request, slug):
	player = Player.objects.get(slug=slug)
	pid = player.player_id
	pl = playercareerstats.PlayerCareerStats(pid).season_totals_regular_season
	stats = pl.get_dict()
	print(pl)
	stats_h = ['Season', 'Team', 'Age', 'GP', 'GS', 'Min', 'FGM', 'FGA', 'FG PCT', 'FG3M', 'FG3A', 'FG3 PCT', 'FTM', 'FTA', 'FT PCT', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS']
	stats_d = stats['data']
	stats_b = []
	for stat in stats_d:
		s = stat[4:]
		s.insert(0, stat[1])
		stats_b.append(s)
	return render(request, 'stats/player_stats.html', {'player': player, 'headers': stats_h, 'stats': stats_b})

# Create your views here.
