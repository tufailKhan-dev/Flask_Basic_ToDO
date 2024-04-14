
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Signup(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100))

    def __init__(self,name):
        self.name = name
   
