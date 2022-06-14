from league import League
from game import Game
from team import Team
import statsapi

#League/Team Table
league = set()
teams = []
teams_data = statsapi.get('teams', {'sportId':1})['teams']
for team in teams_data:
    league.add(League(team['league']['id'], team['league']['name'], team['division']['id'], team['division']['name']))
    teams.append(Team(team['id'], team['name'], team['league']['name'], team['division']['name']))
# print(teams)
# print(league)

season = statsapi.get('season', {'seasonId':2022, 'sportId':1})['seasons'][0]

#Games
games = set()
for item in list(league):
    games_data = statsapi.schedule(start_date='2022-06-09', end_date='2022-06-09')
    for game in games_data:
        double_header = game['doubleheader'] == 'Y'
        games.add(Game(game['game_id'], game['game_date'], game['away_id'], game['home_id'], game['away_probable_pitcher'], game['home_probable_pitcher'], game['away_score'], game['home_score'], double_header))
