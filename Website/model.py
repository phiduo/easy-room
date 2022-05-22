from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(200))
    date = db.Column(db.DateTime)
    from_time = db.Column(db.DateTime)
    to_time = db.Column(db.DateTime)

    def __repr__(self):
        return 'Reservation %r' % self.id

    def __init__(self, name, date, to_time, from_time):
        self.name = name
        self.date = date
        self.to_time = to_time
        self.from_time = from_time

    def __str__(self):
        return self.name + ', ' + str(self.date) + ', ' + str(self.from_time) + ' -->' + str(
            self.to_time)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'date': self.date,
            'from_time': self.from_time,
            'to_time': self.to_time
        }
