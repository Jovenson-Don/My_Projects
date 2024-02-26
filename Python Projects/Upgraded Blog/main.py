from flask import Flask, render_template, request
import requests
import smtplib

API = "https://api.npoint.io/3d1931afa4a8f5e9bf21"
data = requests.get(API).json()

my_email = "joeydon21@gmail.com"
password = ""

app = Flask(__name__)


@app.route("/")
def home_page():
    return render_template("index.html", data=data)


@app.route("/about")
def about_page():
    return render_template("about.html")


@app.route("/post/<int:index>")
def post_page(index):
    post = None
    for blog_post in data:
        if blog_post["id"] == index:
            post = blog_post
    return render_template("post.html", post=post)


@app.route("/contact", methods=["POST", "GET"])
def contact_page():
    if request.method == "POST":
        form = request.form
        email = form["email"]
        name = form["name"]
        message = form["message"]
        phone = form["phone"]
        send_mail(email, phone, name, message)
        return render_template("contact.html")
    else:
        return render_template("contact.html")


def send_mail(name, phone, email, message):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="jovensondon@yahoo.com",
                            msg=f"Subject:Message Received!\n\nName:{name}\nPhone:{phone}\nEmail:{email}\nMessage:{message}")


app.run(debug=True)
