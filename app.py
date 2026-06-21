from flask import Flask, render_template, send_file, request
from main import (top_entities,
                  most_important_entity,
                  most_important_suspect,
                  most_important_witness,
                  most_important_location,
                  most_important_evidence,
                  get_entity_info)

app = Flask(__name__)

entity_info = get_entity_info

@app.route("/")
def home():
    return render_template(
        "index.html",
        top_entities=top_entities,
        most_important_entity=most_important_entity,
        most_important_suspect=most_important_suspect,
        most_important_witness=most_important_witness,
        most_important_location=most_important_location,
        most_important_evidence=most_important_evidence,
        entity_info=entity_info
    )

@app.route("/graph")
def graph():
    return send_file("case_network.html")


app.run(debug=True)