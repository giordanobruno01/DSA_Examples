from flask import Blueprint, render_template, redirect, url_for, request, flash, Flask
from flask_sqlalchemy import SQLAlchemy

main = Flask(__name__) 

@main.route("/") 
def index():
    return render_template("index.html") 

@main.route("/linkedlist")  
def linkedList(): 
    return render_template("linkedlist.html")

@main.route("/linkedlist" , methods = ["POST"])
def linkedList_post():
    return url_for("linkedList")

@main.route("/queue") 
def queue():
    return render_template("queue.html")

@main.route("/queue" , methods = ["POST" ])
def queue_post():
    return url_for("queue")

@main.route("/stack") 
def stack():
    return render_template("stack.html")

@main.route("/stack" , methods = ["POST" ])
def stack_post():
    
    return url_for("stack")


if __name__ == "__main__": 
    main.run(debug=True) 

 