from flask import Blueprint, render_template, redirect, url_for, request, flash, Flask
from flask_sqlalchemy import SQLAlchemy

main = Flask(__name__)

@main.route("/")
def index():
    return render_template("index.html") 

if __name__ == "__main__": 
    main.run(debug=True) 

 