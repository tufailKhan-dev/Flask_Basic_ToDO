from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_workd():
    return "<h1> hello world, i am here</h1>"


@app.route("/<name>")
def user(name):
    return f"<h1>hello {name} how are u?</h1>"

@app.route("/<int:i>")
def page(i):
    return f"<h3>congratulaton u pass</h3>" if i>50 else f"<h2>sorry u fail'd</h2>" 


if __name__ == "__main__":
    app.run(debug=True)