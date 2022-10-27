from app import db


# create new bike class that inherits from db.Model
# going to list out coloumns and what types they are
class Bike(db.Model):
    #not inside any method, directly under Bike:
    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    name = db.Column(db.String)
    price = db.Column(db.Integer)
    size = db.Column(db.Integer)
    type = db.Column(db.String)