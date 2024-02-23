from flask import Flask, render_template
import requests

API = "https://api.npoint.io/3d1931afa4a8f5e9bf21"
data = requests.get(API).json()

app = Flask(__name__)


@app.route("/")
def home_page():
    return render_template("index.html", data=data)


@app.route("/about")
def about_page():
    return render_template("about.html")


@app.route("/contact")
def contact_page():
    return render_template("contact.html")


@app.route("/post/<int:index>")
def post_page(index):
    post = None
    for blog_post in data:
        if blog_post["id"] == index:
            post = blog_post
    return render_template("post.html", post=post)


app.run(debug=True)
