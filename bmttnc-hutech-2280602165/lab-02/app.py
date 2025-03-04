from flask import Flask, render_template, request, json
from cipher.caesar import CaesarCipher

app = Flask(__name__)

# Router routes for home page
@app.route("/")
def home():
    return render_template("index.html")

# Router routes for caesar cipher
@app.route("/caesar")
def caesar():
    return render_template("caesar.html")

