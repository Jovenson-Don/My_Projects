from flask import Flask, render_template, request
import requests
from datetime import datetime

app = Flask("app")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/results", methods=["POST", "GET"])
def receive_stats():
    api = "http://b8c40s8.143.198.70.30.sslip.io/api/PlayerDataTotals/name/"
    date = datetime.now().year
    try:
        player = request.form["player"].strip()
        year = int(request.form["year"])
        data = requests.get(api + player).json()
        player_full_name = data[0]["playerName"]
        for i in data:
            if i["season"] == year:
                ppg = float(format(i["points"] / i["games"], ".1f"))
                apg = float(format(i["assists"] / i["games"], ".1f"))
                rpg = float(format(i["totalRb"] / i["games"], ".1f"))
                spg = float(format(i["steals"] / i["games"], ".1f"))
                bpg = float(format(i["blocks"] / i["games"], ".1f"))
                tpg = float(format(i["turnovers"] / i["games"], ".1f"))
                fgp = format(float(i["fieldPercent"]) * 100, ".1f")
                tpgp = format(float(i["threePercent"]) * 100, ".1f")
                ft = format(float(i["ftPercent"]) * 100, ".1f")

                player_info = f"{player_full_name} averages for the {year} season"
                player_results = f"{ppg}PPG {apg}APG {rpg}RPG {spg}SPG {bpg}BLK {tpg}TOV {fgp}FG {tpgp}3FG {ft}FT"
                return render_template("results.html", results=player_results, results_info=player_info)
            # else:
            #     player_results = (f"{player_full_name} didn't play in that season or the season "
            #                       f"hasn't happened yet.")
            #     return render_template("results.html", results=player_results)
    except ValueError:
        return render_template("index.html")
    except IndexError:
        player_results = f"Player entered never played in nba. Try again.".title()
        return render_template("results.html", results=player_results)


app.run(debug=False, host="0.0.0.0")
