from league import League
from league import League
from team import Team
import statsapi

#League/Team Table
league = set()
teams = []
teams_data = statsapi.get('teams', {'sportId':1})['teams']
for team in teams_data:
    league.add(League(team['league']['id'], team['league']['name'], team['division']['id'], team['division']['name']))
    teams.append(Team(team['id'], team['name'], team['league']['name'], team['division']['name']))
print(teams)
print(league)

#Schedule
