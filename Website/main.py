import json

from flask import Flask, render_template, request, redirect, flash, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///room-reservation.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
db = SQLAlchemy(app)

# insert room
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

@app.route('/reservation', methods = ['GET', 'POST'])
def getForm():
    if request.method == 'POST':
        content = request.form
        name = content['name']
        email = content['email']
        telnr = content['tel']
        date = datetime.strptime(content['date'], '%Y-%m-%d')
        from_time = datetime.strptime(content['from'], '%H:%M')
        to_time = datetime.strptime(content['to'], '%H:%M')
        from_time = datetime.combine(datetime.date(date), datetime.time(from_time))
        to_time = datetime.combine(datetime.date(date), datetime.time(to_time))
        room = content['room']

        r = Reservation(name, email, telnr, date, to_time, from_time, room)

        now = datetime.now()

        #check if valid input
        if (r.from_time > r.to_time) or (r.from_time < now) or (r.to_time < now):
            flash('Time periode is not valid.')
            return redirect('/reservation')


        for reservation in Reservation.query.filter_by(room = r.room):
            if (reservation.from_time <= r.from_time <= reservation.to_time) or (r.from_time <= reservation.from_time <= r.to_time):
                flash('Period is not available.')
                return redirect('/reservation')

        try:
            db.session.add(r)
            db.session.commit()
            return redirect('/done')

        except:
            return 'There is a problem. Try again later.'

    else:
        return render_template('reservation.html')

@app.route('/', methods = ['GET'])
def getIndex():
    return render_template('index.html', title = 'Welcome')

@app.route('/admin', methods = ['GET'])
def getReservations():
    return render_template('admin_overview.html', title = 'Admin Übersicht')

@app.route('/api/data')
def data():
    return {'data': [reservation.to_dict() for reservation in Reservation.query]}

@app.route('/isAvailable/<room>')
def display(room):
    if not rooms.__contains__(room):
        return 'No room with name ' + room
    now = datetime.now()
    reservations = Reservation.query.filter_by(room = room)
    for reservation in reservations:
        if reservation.from_time <= now <= reservation.to_time:
            return 'False'
    return 'True'

@app.route('/admin/delete', methods = ['POST'])
def delete():
    reservation_to_delete = int(request.form['ID'])
    try:
        Reservation.query.filter_by(id=reservation_to_delete).delete()
        db.session.commit()
        flash('Reservation deleted successfully.')
        return redirect('/admin')
    except:
        flash('There was a problem with deleting the reservation.')
        return redirect('/admin')

@app.route('/done', methods = ['GET'])
def returnThankYou():
    return render_template('done.html', title = 'Thank you!')

if __name__ == "__main__":
    app.run(debug=True)