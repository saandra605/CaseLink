from flask import Flask, render_template, send_file

app = Flask(__name__)

@app.route("/")

def home():
    return render_template("index.html")

@app.route("/graph")
def graph():
    return send_file("case_network.html")

app.run(debug=True)