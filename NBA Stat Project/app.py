from flask import Flask, render_template, request
import requests
from datetime import datetime

app = Flask("app")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/results", methods=["POST", "GET"])
def receive_stats():
    api = "https://nba-stats-db.herokuapp.com/api/playerdata/name/"
    date = datetime.now().year - 1

    try:
        player = request.form["player"].strip()
        year = int(request.form["year"])
        data = requests.get(api + player).json()
        results = data["results"]
        player_full_name = results[0]["player_name"]
        if date - year < 0 or date - year > data["count"]:
            player_results = (f"{player_full_name} didn't play in that season or the season "
                              f"hasn't happened yet.")
            return render_template("results.html", results=player_results)
        else:
            ppg = float(format(results[date - year]["PTS"] / results[date - year]["games"], ".1f"))
            apg = float(format(results[date - year]["AST"] / results[date - year]["games"], ".1f"))
            rpg = float(format(results[date - year]["TRB"] / results[date - year]["games"], ".1f"))
            spg = float(format(results[date - year]["STL"] / results[date - year]["games"], ".1f"))
            bpg = float(format(results[date - year]["BLK"] / results[date - year]["games"], ".1f"))
            tpg = float(format(results[date - year]["TOV"] / results[date - year]["games"], ".1f"))
            fgp = format(float(results[date - year]["field_percent"]) * 100, ".1f")
            player_info = f"{player_full_name} averages for the {year} season"
            player_results = f"{ppg}PPG {apg}APG {rpg}RPG {spg}SPG {bpg}BLK {tpg}TOV {fgp}FG"
            print(player_results)
            return render_template("results.html", results=player_results, results_info=player_info)
    except ValueError:
        return render_template("index.html")
    except IndexError:
        player_results = f"Player entered never played in nba. Try again.".title()
        return render_template("results.html", results=player_results)


app.run(debug=False, host="0.0.0.0")
