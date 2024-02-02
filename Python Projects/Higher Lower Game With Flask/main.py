from flask import Flask
from random import randint

app = Flask("app.py")
random_number = randint(0, 9)


@app.route("/")
def start_game():
    return ("<h1>Guess a number between 0 and 9</h1>"
            "<img src=https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif>")


@app.route("/<int:number>")
def guess_number(number):
    if number == random_number:
        return (f"<h1>and {number} is just right:</h1>"
                f"<img src=https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif>")
    if number < random_number:
        return (f"<h1>{number} is too low:</h1>"
                f"<img src=https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif>")
    else:
        return (f"<h1>{number} is too high: </h1>"
                f"<img src=https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif>")


app.run(debug=True)
