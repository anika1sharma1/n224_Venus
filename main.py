from flask import Flask, render_template, request

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

@app.route("/christina/")
def christina():
    return render_template("team/christina.html")

@app.route("/gigi/")
def gigi():
    return render_template("team/gigi.html")

# from image import hide_msg
# @app.route("/rgbhide")
# def hidemsg():
#    hide_msg()

if __name__ == "__main__":
    app.run(debug=True)