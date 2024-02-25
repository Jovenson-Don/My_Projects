import requests
from datetime import datetime


def grab_stats():
    api = "https://nba-stats-db.herokuapp.com/api/playerdata/name/"
    response = requests.get(api + player).json()
    return response


is_on = True
year = None
player_full_name = None

while is_on:
    try:
        while True:
            player = input(str("Enter a player name: ").title())
            if not any(char.isdigit() for char in player):
                break
            print("Please enter a player without any numbers. Try again.")
        date = datetime.now().year - 1
        year = int(input("Which season? "))
        data = grab_stats()
        player_full_name = data["results"][0]["player_name"]
        results = data["results"][date - year]

        if data["count"] == 0:
            print(f"This {player_full_name} does not exist. Try again.")
        elif date - year <= -1:
            print(f"Season did not happen yet try again. Try again.")
        else:
            ppg = float(format(results["PTS"] / results["games"], ".2f"))
            apg = float(format(results["AST"] / results["games"], ".2f"))
            rpg = float(format(results["TRB"] / results["games"], ".2f"))
            spg = float(format(results["STL"] / results["games"], ".2f"))
            bpg = float(format(results["BLK"] / results["games"], ".2f"))
            tpg = float(format(results["TOV"] / results["games"], ".2f"))
            fgp = format(float(results["field_percent"]) * 100, ".2f")
            print(f"{player_full_name} averages for {year} season: {ppg}PPG, {apg}APG, {rpg}RPG, "
                  f"{spg}SPG, {bpg}BLK, {tpg}TOV {fgp}FG")
    except ValueError:
        print("Enter a number for year. Try again.")
    except IndexError:
        print(f"{player_full_name} did not play in the {year} season. Try again.")
