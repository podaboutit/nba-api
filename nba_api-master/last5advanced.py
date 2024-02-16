from nba_api.stats.endpoints import teamgamelogs
from nba_api.stats.endpoints import boxscoreadvancedv2
import pandas as pd

teams = teamgamelogs.TeamGameLogs().get_data_frames()[0]
team_name = "Magic"
# get the team ID from the team name
team_id = [team["id"] for team in teams if team["nickname"] == team_name][0]
season = "2023-24"
last_n_games = 5
location = ""
season_type = "Regular Season"

team_gamelogs = teamgamelogs.TeamGameLogs(team_id_nullable=team_id, season_nullable=season, last_n_games_nullable=last_n_games, location_nullable=location, season_type_nullable=season_type)
team_gamelogs_df = team_gamelogs.get_data_frames()[0]

# use boxscoreadvancedv2 to fetch the advanced boxscores for each game and save the team advanced stats to a dataframe
team_advanced_stats = []
for game_id in team_gamelogs_df["GAME_ID"]:
    try:
        boxscore_advanced = boxscoreadvancedv2.BoxScoreAdvancedV2(game_id=game_id)
        boxscore_advanced_df = boxscore_advanced.get_data_frames()[0]
        # select the desired team advanced stats columns from the dataframe
        team_advanced_stats.append(boxscore_advanced_df.loc[0, ["GAME_ID", "TEAM_ID", "OFF_RATING", "DEF_RATING"]])
    except Exception as e:
        print(f"Error fetching data for game ID {game_id}: {str(e)}")

# convert the list of team advanced stats to a dataframe
team_advanced_stats_df = pd.concat(team_advanced_stats)

print(team_advanced_stats_df)
