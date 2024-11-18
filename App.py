from flask import Flask
from flask import render_template,request

App = Flask("__name__")

@App.route("/",methods=["GET","POST"])
def index():
    return(render_template("index.html"))

if __name__ == "__main__":
    App.run()
