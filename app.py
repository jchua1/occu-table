from flask import Flask, render_template
import csv
from random import choice, uniform

app = Flask(__name__)

occs = {}
links = {}

def readToDict():
    import csv
    with open("occupations.csv") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            job = row["Job Class"]
            percent = float(row["Percentage"])
            link = row["Link"]
            if (job != "Total"):
                occs[job] = [percent, link]
                links[job] = link
                
def pickWeighted():
    rand = uniform(0, 99.8)
    x = 0.0
    for job, value in occs.iteritems():
        x += value[0]
        if rand <= x:
            return job
    return job

@app.route("/")
def direct():
    return render_template("main.html", link = "/occupations")

@app.route("/occupations")                
def tablefy():
    readToDict()
    j = pickWeighted()
    l = occs[j][1]
    return render_template("temp.html", title = "Occupation Table", table = occs, job = j, link = l)

if __name__ == "__main__":
    #app.debug = True
    app.run()
