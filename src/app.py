from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def home_page():
    return render_template(
        "home.html",
        title="Welcome to sendbits.to!",
        description="Share all your crypto wallets easily with just one link."
    )


@app.route('/<username>')
def template(username):
    return render_template(
        'user.html',
        username=username,
        title=f"Send Crypto to {username}",
        description="Smarter page templates with Flask & Jinja."
    )
