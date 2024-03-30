from flask import Blueprint, render_template, redirect, url_for, request, flash, Flask
import os
from stackFile import stackClass
from flask_sqlalchemy import SQLAlchemy

main = Flask(__name__) 
main.config["UPLOAD_FOLDER"] = "files" 
obj = stackClass()
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

@main.route("/stack", methods = ["get"]) 
def stack():
    return render_template("stack.html", text = obj.display())

@main.route("/stack" , methods = ["POST", "get"])
def stack_post():

    javaFile = request.files["javaFile"]
    javaFile.save(os.path.join(main.config['UPLOAD_FOLDER'],javaFile.filename))
    j = open(os.path.join(main.config['UPLOAD_FOLDER'],javaFile.filename),"r")
   
    line = 1
    while True:
        code = j.readline()
        if code == '':
            break

        obj.processor(code, line)
        line +=1
    global text 
    text = obj.display()
    return url_for("stack")
     
    
    # return url_for("stack", text = javaFile.read())
if __name__ == "__main__": 
    main.run(debug=True) 

 