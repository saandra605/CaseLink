from flask import Flask, render_template, send_file, request
from main import (top_entities,
                  most_important_entity,
                  most_important_suspect,
                  most_important_witness,
                  most_important_location,
                  most_important_evidence,
                  get_entity_info,
                  total_entities,
                  total_communities,
                  total_relationships
                )

app = Flask(__name__)

entity_info = get_entity_info

@app.route("/")
def home():

    entity = request.args.get("entity", "Marcus White")

    entity_info = get_entity_info(entity)


    return render_template(
        "index.html",
        top_entities=top_entities,
        most_important_entity=most_important_entity,
        most_important_suspect=most_important_suspect,
        most_important_witness=most_important_witness,
        most_important_location=most_important_location,
        most_important_evidence=most_important_evidence,
        entity_info=entity_info,
        total_entities=total_entities,
        total_relationships=total_relationships,
        total_communities=total_communities
    )

@app.route("/graph")
def graph():
    return send_file("case_network.html")


app.run(debug=True)