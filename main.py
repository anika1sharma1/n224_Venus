from flask import Flask, render_template, request
import requests
import json


# create an instance of flask object
app = Flask(__name__)


# home page accessed with http://127.0.0.1:5000/
@app.route("/")
# map URL route for function below
def index():
    return render_template("index.html")

@app.route("/journal/")
def journal():
    return render_template("journals/journal.html")

@app.route("/about/")
def about():
    return render_template("layouts/about.html")

@app.route("/christina/", methods=['GET', 'POST'])
def christina():
    place="Atlanta"
    if request.method == 'POST':
        place = request.form['place']
    querystring = {"q":place}

    url = "https://weatherapi-com.p.rapidapi.com/current.json"

    headers = {
        'x-rapidapi-host': "weatherapi-com.p.rapidapi.com",
        'x-rapidapi-key': "35c993f134msh6fbb5b79c410a17p11f3f7jsn6ad7e30cfe36"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    output = json.loads(response.text)
    print(response.text)
    return render_template("team/christina.html", detail=output)

@app.route("/gigi/")
def gigi():
    url = "https://random-words-with-pronunciation.p.rapidapi.com/word"

    headers = {
        'x-rapidapi-host': "random-words-with-pronunciation.p.rapidapi.com",
        'x-rapidapi-key': "4ab4681ba9mshf17197c9d59be44p17d1edjsnabe7ccc22eb5"
    }

    response = requests.request("GET", url, headers=headers)
    output = json.loads(response.text)
    print(response.text)
    return render_template("team/gigi.html", Y=output)

@app.route("/anika/")
def anika():
    return render_template("team/anika.html")

@app.route("/allison/")
def allison():
    return render_template("team/allison.html")

@app.route("/neha/")
def neha():
    return render_template("team/neha.html")

# from image import hide_msg
# @app.route("/rgbhide")
# def hidemsg():
#    hide_msg()

if __name__ == "__main__":
    app.run(debug=True)