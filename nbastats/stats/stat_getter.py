from nba_api.stats.static import players
from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.library.parameters import SeasonType
from bs4 import BeautifulSoup
import requests

def career_stats(pid, per_mode):
	pl = playercareerstats.PlayerCareerStats(per_mode36=per_mode, player_id=pid).season_totals_regular_season
	stats = pl.get_dict()
	stats_h = ['Season', 'Team', 'Age', 'GP', 'GS', 'Min', 'FGM', 'FGA', 'FG PCT', 'FG3M', 'FG3A', 'FG3 PCT', 'FTM',
			   'FTA', 'FT PCT', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS']
	stats_d = stats['data']
	stats_b = []
	for stat in stats_d:
		s = stat[4:]
		s.insert(0, stat[1])
		s[2] = int(s[2])
		stats_b.append(s)
	return stats_h, stats_b


