from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('main_page.html')


@app.route("/guesso")
def guesso():
    return "<p>GUESSO page!</p>"

@app.route("/engenerate")
def generate():
    return "<p>enGENERATE page!</p>"

@app.route("/info")
def info():
    return "<p>info page!</p>"