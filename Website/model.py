from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# rooms
rooms = ['room1', 'room2']

class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String(200))
    email = db.Column(db.String(300))
    telnr = db.Column(db.Integer)
    date = db.Column(db.DateTime)
    to_time = db.Column(db.DateTime)
    from_time = db.Column(db.DateTime)
    room = db.Column(db.String(50))

    def __repr__(self):
        return 'Reservation %r' %self.id

    def __init__(self, name, email, telnr, date, to_time, from_time, room):
        self.name = name
        self.email = email
        self.telnr = telnr
        self.date = date
        self.to_time = to_time
        self.from_time = from_time
        self.room = room

    def __str__(self):
        return self.name + ', ' + str(self.date) + ', ' + str(self.from_time) + ' -->' + str(self.to_time) + ", " + self.room

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'telnr': self.telnr,
            'date': self.date,
            'from_time': self.from_time,
            'to_time': self.to_time,
            'room': self.room
        }