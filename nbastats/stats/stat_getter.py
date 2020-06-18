from nba_api.stats.static import players
from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.library.parameters import SeasonType
from nba_api.stats.static import teams
from nba_api.stats.endpoints import teamyearbyyearstats
from nba_api.stats.endpoints import PlayerDashboardByGeneralSplits
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

def team_year_by_year(tid, per_mode):
	team = teamyearbyyearstats.TeamYearByYearStats(per_mode_simple=per_mode, team_id=tid)
	team_stats = team.get_dict()
	headers = ['Team', 'Year', 'GP', 'Wins', 'Losses', 'Win %', 'Conf Rank', 'Div Rank', 'PO Wins', 'PO Losses',
			   'Conf Count', 'Div Count', 'Finals Appearance', 'FGM', 'FGA', 'FG PCT', 'FG3M', 'FG3A', 'FG3 PCT', 'FTM',
			   'FTA', 'FT PCT', 'OREB', 'DREB', 'REB', 'AST', 'PF', 'STL', 'TOV', 'BLK', 'PTS', 'PTS Rank']
	stats_d = team_stats['resultSets'][0]['rowSet']
	stats = []
	for stat in stats_d:
		team_name = stat[1] + ' ' + stat[2]
		s = stat[3:]
		s.insert(0, team_name)
		stats.append(s)
	return headers, stats

def player_dashboard_general_splits(pid, per_mode, detail):
	detail_dict = {
		'overall': 0,
		'location': 1,
		'wins-losses': 2,
		'month': 3,
		'all-star': 4,
		'starting position': 5,
		'days rest': 6
	}
	player = PlayerDashboardByGeneralSplits(player_id=pid, per_mode_detailed=per_mode)
	player = player.get_data_frames()[detail_dict['month']]
	headers = player.axes[1]
	stats = player.values
	return headers, stats




