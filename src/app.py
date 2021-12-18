from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def home_page():
    return render_template(
        "home.html"
    )


@app.route("/login")
def login_page():
    return render_template(
        "login.html"
    )


@app.route("/register")
def register_page():
    return render_template(
        "register.html"
    )


@app.route('/<username>')
def template(username):
    return render_template(
        'user.html',
        username=username,
        title=f"Send Crypto to {username}",
        description="Smarter page templates with Flask & Jinja."
    )
