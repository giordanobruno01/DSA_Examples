from flask import Blueprint, render_template, redirect, url_for, request, flash, Flask
import os
from stackFile import stackClass
from queueFile import passenger, queue
from linkedFile import item, linkedList
from flask_sqlalchemy import SQLAlchemy

main = Flask(__name__) 
main.config["UPLOAD_FOLDER"] = "files" 
main.config["SECRET_KEY"] = "HELLO"
obj = stackClass()
queueObj = queue(5)  
llObj = linkedList()
message = ""
linkMessage = ''   
@main.route("/") 
def index():
    return render_template("index.html") 

@main.route("/linkedlist")   
def linkedList():  
    lists = llObj.getItems()
    global linkMessage
    return render_template("linkedlist.html", listItem = lists, lenItem = len(lists),  linkMessage = linkMessage)

@main.route("/linkedlist" , methods = ["POST"])
def linkedList_post():
    textInput = request.form.get("textInput")
    choice = request.form.get("choice")
    listItem = request.form.get("listItem")
    if choice == "add": 
        if textInput == "":
            llObj.message = "No text input"
        else:
            llObj.add(textInput)
    elif choice == "addbefore" or choice == "addafter":
        if listItem == "" and textInput == "":
            llObj.message = "select an option and give an input" 
        elif textInput == "":
            llObj.message = "No text input"
        elif listItem == "":
            llObj.message = "select an option"
        else:
            llObj.add(textInput)

    
    return url_for("linkedList") 

@main.route("/queue") 
def queue():
    global message
    if message != "":
        flash(message) 
    return render_template("queue.html", passagerList = queueObj.passengerList)

@main.route("/queue" , methods = ["POST" ])
def queue_post(): 
    global message
    name = request.form.get("name") 
    origin = request.form.get("origin")
    destination = request.form.get("destination")
    weight = request.form.get("weight")
    if origin == None:
        pass
    else:
        pasgr = passenger(name=name, origin=origin, destination=destination, weight=weight)
        message = queueObj.enqueue(pasgr)
        
    return redirect(url_for("queue"))

@main.route("/checkout" , methods = ["POST" ]) 
def checkout():
    global message
    message = queueObj.dequeue()
    return 1

@main.route("/stack")  
def stack():
    return render_template("stack.html" , text = "reload")

@main.route("/stack" , methods = ["POST", "get"])
def stack_post(): 

    javaFile = request.files["javaFile"]
    javaFile.save(os.path.join(main.config['UPLOAD_FOLDER'],javaFile.filename))
    j = open(os.path.join(main.config['UPLOAD_FOLDER'],javaFile.filename),"r")
    multiline = False
    line = 1
    while obj.display() == "No error found":
        code = j.readline()
        if code == '':  
            break 
        if "//" in code:
            code = code.split("//")[0]

        if "/*" in code and "*/" in code:
            code = code.split("/*")[0] + " "+ code.split("*/")[1] 

        if "/*" in code:
            code = code.split("/*")[0]
            multiline = True
        elif multiline == True and "*/" not in code: 
            line +=1
            continue
        elif multiline == True and "*/" in code:
            multiline = False
            code = code.split("/*")[1]
 
            
        obj.processor(code, line)
        line +=1 
           

    if len(obj.stack)!=0 and obj.display()=="No error found":
        return render_template("stack.html", text = f"This bracket '{obj.stack[obj.top][0]}' at line {obj.stack[obj.top][2]} with the code  '{obj.stack[obj.top][1]}' is not being closed correctly")
    else:
        return render_template("stack.html", text = obj.display())
    
    # return url_for("stack", text = javaFile.read())


if __name__ == "__main__": 
    main.run(debug=True) 

 