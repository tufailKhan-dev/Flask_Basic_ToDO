
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100))
    userdata = db.Column(db.String(100))

    def __init__(self,name,userdata):
        self.name = name
        self.userdata = userdata
