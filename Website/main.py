from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///room-reservation.db'
db = SQLAlchemy(app)


class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(200))
    email = db.Column(db.String(300))
    telnr = db.Column(db.Integer)
    dateFrom = db.Column(db.DateTime)
    dateTo = db.Column(db.DateTime)
    room = db.Column(db.String(50))

    def __repr__(self):
        return 'Reservation %r' % self.id

    def __init__(self, name, email, telnr, dateFrom, dateTo, room):
        self.name = name
        self.email = email
        self.telnr = telnr
        self.dateFrom = dateFrom
        self.dateTo = dateTo
        self.room = room

    def __str__(self):
        return self.name + ', ' + str(self.dateFrom) + ' -->' + str(self.dateTo) + ", " + self.room


@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        content = request.form
        name = content['Name']
        email = content['E-Mail']
        telnr = content['Telefon']
        dateFrom = datetime.strptime(content['Von'], '%Y-%m-%dT%H:%M')
        dateTo = datetime.strptime(content['Bis'], '%Y-%m-%dT%H:%M')
        room = content['Raum']

        r = Reservation(name, email, telnr, dateFrom, dateTo, room)

        try:
            db.session.add(r)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue...'

    else:
        reservations = Reservation.query.order_by(Reservation.id)
        return render_template('index.html')


@app.route('/admin', methods=['GET'])
def getReservations():
    reservations = Reservation.query.all()
    l = []
    for r in reservations:
        l.append(str(r))
    return str(l)


if __name__ == "__main__":
    app.run(debug=True)
