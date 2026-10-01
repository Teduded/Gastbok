from flask import Flask, render_template, request, redirect
import json
import os
from datetime import datetime

app = Flask(__name__)

FIL = os.path.join(os.path.dirname(__file__), "inlagg.json")


def hamta_inlagg():
    with open(FIL, "r", encoding="utf-8") as fil:
        return json.load(fil)


@app.route("/")
def index():
    inlagg = hamta_inlagg()

    return render_template(
        "index.html",
        inlagg=inlagg
    )


@app.route("/spara", methods=["POST"])
def spara():
    namn = request.form["namn"]
    meddelande = request.form["meddelande"]

    nytt_inlagg = {
        "namn": namn,
        "meddelande": meddelande,
        "tid": datetime.now().strftime("%Y-%m-%d %H:%M")
    }

    inlagg = hamta_inlagg()

    inlagg.append(nytt_inlagg)

    with open(FIL, "w", encoding="utf-8") as fil:
        json.dump(inlagg, fil, ensure_ascii=False, indent=4)

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)