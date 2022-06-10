from team import Team
import statsapi

#Team Table
teams = []
teams_data = statsapi.get('teams', {'sportId':1})['teams']
for team in teams_data:
    teams.append(Team(team['id'], team['name'], team['league']['name'], team['division']['name']))
print(teams)
