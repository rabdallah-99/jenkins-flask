from application import db

class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    completed = db.Column(db.Boolean, default=False)