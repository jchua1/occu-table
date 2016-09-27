from flask import Flask, render_template
from utils import dict

app = Flask(__name__)

@app.route("/")
def direct():
    return render_template("main.html", link = "/occupations")

@app.route("/occupations")
def tablefy():
    j = dict.pickWeighted()
    l = dict.getLink(j)
    return render_template("temp.html", title = "Occupation Table", table = dict.occs, job = j, link = l)

if __name__ == "__main__":
    app.debug = True
    app.run()
