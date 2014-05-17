from manage import db


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    rating = db.Column(db.Integer)

    def __init__(self, name, rating):
        self.name = name
        self.rating = rating
