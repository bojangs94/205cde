from flask import Flask, render_template, request
import os
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def index():
    return render_template("about.html")

@app.route("/contact")
def index():
    return render_template("contact.html")

@app.route("/gallery")
def index():
    return render_template("gallery.html")

@app.route("/history")
def index():
    return render_template("history.html")
    
if__name__ == "__main__":
    app.debug = True
    port = int(os.getenv('PORT', 8080))
    host = os.getenv('IP', '0.0.0.0')
    app.run(port=port, host=host)