from flask import Flask, render_template
import main

app = Flask("app")


@app.route("/")
def home():
    return render_template("index.html", player=main.player)


app.run(debug=False)
