#html with GET POST

# jinja2 template engine
"""
{% %} {% end %}  for statement ,conditions

{{ }} variables

{#    #} this is for comment 
 

"""



# @app.route("/")
# def hello_workd():
#     return render_template("index.html")


# @app.route("/<name>")
# def user(name):
#     return f"<h1>hello {name} how are u?</h1>"

# @app.route("/<int:i>")
# def page(i):
#     return f"<h3>congratulaton u pass</h3>" if i>50 else f"<h2>sorry u fail'd</h2>" 

# @app.route("/success/<int:score>")
# def success(score):
#     res = ""
#     if score > 35:
#         res ="Pass"
#     else:
#         res = "Fail"
#     feed = {'result':res , 'score':score} 
#     return render_template("result.html", Feed = feed)


# @app.route("/fail/<int:score>")
# def fail(score):
#     return f"given {score}% is not greater then 35%, Fail!"

# @app.route("/submit", methods=["POST","GET"])
# def submit():
#     total_score = 0
#     if request.method == "POST":
#         science = float(request.form['science'])
#         math = float(request.form['math'])
#         chemistry = float(request.form['chemistry'])
#         total_score = (science + math + chemistry)/3
#     res = "success"
    
#     return redirect(url_for(res,score=total_score))

from flask import Flask, redirect, render_template, request, url_for, session
from datetime import timedelta

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__,template_folder="templates")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRANK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100))
    userdata = db.Column(db.String(100))

    def __init__(self,name,userdata):
        self.name = name
        self.userdata = userdata




app.secret_key = "aslkalsd"
# registration page
@app.route("/")
def index():
    
        
    todo_data = Todo.query.all()
    return render_template("index.html", todos = todo_data)


#authentication
@app.route("/login",methods= ["POST"])
def login():
    if request.method == "POST":
        name = request.form.get("username")
        session['name'] = name
        return redirect(url_for("result",user=name))
    return redirect(url_for("index"))

#logout
@app.route("/logout")
def logout():
    session.pop('name',None)
    return redirect(url_for("index"))


#main page
@app.route("/<user>")
def result(user):
    if 'name' in session:
        name = session['name']
        return render_template("result.html", name=name)
    return render_template("index.html")



if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        app.run(debug=True)
   