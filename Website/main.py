
from flask import Flask, render_template, request, redirect, flash
from datetime import datetime
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from model import Reservation, db, rooms

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///room-reservation.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# init app
db.init_app(app)

# admin
admin = Admin(app)
admin.add_view(ModelView(Reservation, db.session))

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

@app.route('/done', methods = ['GET'])
def returnThankYou():
    return render_template('done.html', title = 'Thank you!')

if __name__ == "__main__":
    app.run(debug=True)