from flask import Flask, render_template, request
import requests
from datetime import datetime

app = Flask("app")

api = "https://nba-stats-db.herokuapp.com/api/playerdata/name/"

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/stats", methods=["POST", "GET"])
def receive_stats():
    player = request.form["player"]
    year = request.form["year"]
    data = requests.get(api + player).json()
    results = data["results"][0]
    player_full_name = results["player_name"]
    ppg = float(format(results["PTS"] / results["games"], ".1f"))
    apg = float(format(results["AST"] / results["games"], ".1f"))
    rpg = float(format(results["TRB"] / results["games"], ".1f"))
    spg = float(format(results["STL"] / results["games"], ".1f"))
    bpg = float(format(results["BLK"] / results["games"], ".1f"))
    tpg = float(format(results["TOV"] / results["games"], ".1f"))
    fgp = format(float(results["field_percent"]) * 100, ".1f")
    return (f"<h1>{player_full_name} averages for {year} season: {ppg}PPG, {apg}APG, "
            f"{rpg}RPG, {spg}SPG, {bpg}BLK, {tpg}TOV {fgp}FG</h1>")




app.run(debug=False)
