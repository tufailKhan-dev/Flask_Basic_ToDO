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

from flask import Flask, flash, redirect, render_template, request, url_for, session, jsonify
from datetime import timedelta
from flask import Flask
from models.userdb import db,User,Todo
app = Flask(__name__,template_folder="templates",static_folder="static")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRANK_MODIFICATIONS'] = False
db.init_app(app)
app.secret_key = "aslkalsd"


#--------------authentication------------------------------

# registration page
@app.route("/")
def index():    
    return render_template("index.html")

#check login
@app.route("/login",methods= ["POST"])
def login():
    if request.method == "POST":
        name = request.form.get("username")
        user_exist = db.session.query(User.query.filter(User.name==name).exists()).scalar()
        if user_exist:
            session['name'] = name
            return redirect(url_for("result", user=name))
        else:
            flash('invalid user', 'error')
            return redirect(url_for("index"))
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




#--------------- todo functions ------------------------------------
#fetch todo data
@app.route("/todos", methods=["GET"])
def get_todo():
    todos = Todo.query.all()
    todo_list = [{'id': todo.id, 'title': todo.title, 'completed': todo.completed} for todo in todos]
    return jsonify(todo_list)

@app.route('/todos', methods=['POST'])
def create_todo():
    data = request.get_json()
    new_todo = Todo(title=data['title'], user_id=data['user_id'])
    db.session.add(new_todo)
    db.session.commit()
    return jsonify({'message': 'Todo created successfully'})


@app.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    todo = Todo.query.get(todo_id)
    if todo:
        data = request.json
        todo.title = data['title']
        todo.completed = data['completed']
        db.session.commit()
        return jsonify({'message': 'Todo updated successfully'})
    else:
        return jsonify({'error': 'Todo not found'}), 404

@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    todo = Todo.query.get(todo_id)
    if todo:
        db.session.delete(todo)
        db.session.commit()
        return jsonify({'message': 'Todo deleted successfully'})
    else:
        return jsonify({'error': 'Todo not found'}), 404

if __name__ == "__main__":
    with app.app_context():
        
        db.create_all()
        app.run(debug=True)
   