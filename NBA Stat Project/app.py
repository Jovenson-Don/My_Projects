from flask import Flask, render_template, request
import requests

app = Flask("app")

# Base API URL
API_URL = "http://b8c40s8.143.198.70.30.sslip.io/api/PlayerDataTotals/name/"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/results", methods=["POST"])
def receive_stats():

    try:
        # Get player and year from the form
        player = request.form["player"].strip()
        year = int(request.form["year"])

        # Fetch player data
        response = requests.get(API_URL + player)
        response.raise_for_status()
        data = response.json()

        # Extract player full name
        player_full_name = data[0]["playerName"]

        # Find stats for the given year
        season_stats = next((i for i in data if i["season"] == year), None)

        if season_stats:
            # Calculate per-game stats
            stats = {
                "ppg": round(season_stats["points"] / season_stats["games"], 1),
                "apg": round(season_stats["assists"] / season_stats["games"], 1),
                "rpg": round(season_stats["totalRb"] / season_stats["games"], 1),
                "spg": round(season_stats["steals"] / season_stats["games"], 1),
                "bpg": round(season_stats["blocks"] / season_stats["games"], 1),
                "tpg": round(season_stats["turnovers"] / season_stats["games"], 1),
                "fgp": round(season_stats["fieldPercent"] * 100, 1),
                "tpgp": round(season_stats["threePercent"] * 100, 1),
                "ft": round(season_stats["ftPercent"] * 100, 1),
            }

            # Generate results strings
            player_info = f"{player_full_name} averages for the {year} season"
            player_results = (
                f"{stats['ppg']} PPG, {stats['apg']} APG, {stats['rpg']} RPG, "
                f"{stats['spg']} SPG, {stats['bpg']} BLK, {stats['tpg']} TOV, "
                f"{stats['fgp']}% FG, {stats['tpgp']}% 3FG, {stats['ft']}% FT"
            )
            return render_template("results.html", results=player_results, results_info=player_info)
        else:
            # No stats found for the given year
            error_message = f"{player_full_name} didn't play in the {year} season."
            return render_template("results.html", results=error_message)

    except (ValueError, IndexError):
        # Handle invalid inputs or player not found
        error_message = "Invalid input or player not found. Please try again."
        return render_template("results.html", results=error_message)

    except requests.RequestException:
        # Handle API request errors
        error_message = "An error occurred while fetching player data. Please try again later."
        return render_template("results.html", results=error_message)


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0")
