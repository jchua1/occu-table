import csv
from random import choice, uniform

occs = {}

def readToDict():
    import csv
    with open("data/occupations.csv") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            job = row["Job Class"]
            percent = float(row["Percentage"])
            link = row["Link"]
            if (job != "Total"):
                occs[job] = [percent, link]
                
def pickWeighted():
    rand = uniform(0, 99.8)
    x = 0.0
    for job, value in occs.iteritems():
        x += value[0]
        if rand <= x:
            return job
    return job

def getLink(job):
    return occs[job][1]
