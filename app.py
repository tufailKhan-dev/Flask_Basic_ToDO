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
from datetime import timedelta,datetime
app = Flask(__name__)
app.secret_key = "aslkalsd"
# app.permanent_session_lifetime = timedelta(minutes=2)


@app.route("/")
def index():
    return render_template("index.html")



@app.before_request
def update_last_activity():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=2)  # Set session lifetime
    session['last_activity'] = datetime.now()



def is_user_inactive():
    last_activity = session['last_activity']
    if last_activity:
        inactive_duration = datetime.now() - last_activity
        if inactive_duration > timedelta(minutes=2):
            return True
    return False


@app.route("/check_activity")
def check_activity():
    if is_user_inactive():
        return redirect(url_for("logout"))



@app.route("/login", methods = ["GET","POST"])
def login():
    if request.method == 'POST':
        name = request.form["username"]
        session['name'] = name
        return redirect(url_for("result"))
    else:
        return render_template("index.html")



@app.route("/result", methods=["POST","GET"])
def result():
    data = []
    if "name" in session:
        name = session["name"]
        if request.method == "POST":
            d = request.form.get("inputdata")
            data.append(d)
        dat = { "data" : data,
               "name" : name}
        return render_template("result.html", dat = dat)
    else:
        return redirect(url_for("login"))
@app.route("/logout")
def logout():
    session.pop("name", None)
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)