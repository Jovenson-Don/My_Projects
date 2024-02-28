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
        if data["count"] == 0:
            return f"<h1>{player} never played in nba</h1>".title()
        elif date - year < 0 or date - year > data["count"]:
            return f"<h1>{player_full_name} didn't play in that season or the season hasn't happened yet.</h1>"
        else:
            ppg = float(format(results[date - year]["PTS"] / results[date - year]["games"], ".1f"))
            apg = float(format(results[date - year]["AST"] / results[date - year]["games"], ".1f"))
            rpg = float(format(results[date - year]["TRB"] / results[date - year]["games"], ".1f"))
            spg = float(format(results[date - year]["STL"] / results[date - year]["games"], ".1f"))
            bpg = float(format(results[date - year]["BLK"] / results[date - year]["games"], ".1f"))
            tpg = float(format(results[date - year]["TOV"] / results[date - year]["games"], ".1f"))
            fgp = format(float(results[date - year]["field_percent"]) * 100, ".1f")
            return (f"<h1>{player_full_name} averages for the {year} season: {ppg}PPG, {apg}APG, "
                    f"{rpg}RPG, {spg}SPG, {bpg}BLK, {tpg}TOV {fgp}FG</h1>")
    except ValueError:
        return render_template("index.html")


app.run(debug=False, host="0.0.0.0")
