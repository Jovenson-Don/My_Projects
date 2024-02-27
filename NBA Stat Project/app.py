from flask import Flask, render_template, request
import requests
from datetime import datetime

app = Flask("app")

api = "https://nba-stats-db.herokuapp.com/api/playerdata/name/"
date = datetime.now().year - 1


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/results", methods=["POST", "GET"])
def receive_stats():
    player = request.form["player"]
    year = int(request.form["year"])
    try:
        data = requests.get(api + player).json()
        results = data["results"]
        if date-year < 0 or date-year > data["count"]:
            return "<h1> No stats for that season or season didn't happen yet</h1>"
        else:
            ppg = float(format(results[date-year]["PTS"] / results[date-year]["games"], ".1f"))
            apg = float(format(results[date-year]["AST"] / results[date-year]["games"], ".1f"))
            rpg = float(format(results[date-year]["TRB"] / results[date-year]["games"], ".1f"))
            spg = float(format(results[date-year]["STL"] / results[date-year]["games"], ".1f"))
            bpg = float(format(results[date-year]["BLK"] / results[date-year]["games"], ".1f"))
            tpg = float(format(results[date-year]["TOV"] / results[date-year]["games"], ".1f"))
            fgp = format(float(results[date-year]["field_percent"]) * 100, ".1f")
            return (f"<h1>{player} averages for the {year} season: {ppg}PPG, {apg}APG, "
                    f"{rpg}RPG, {spg}SPG, {bpg}BLK, {tpg}TOV {fgp}FG</h1>")
    except IndexError:
        return f"<h1>{player} never played in nba</h1>".title()


app.run(debug=False)
