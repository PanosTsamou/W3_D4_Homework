from flask import render_template,request
from app import app
from models.events import events , add_new_event
from models.event import *

@app.route('/events')
def index():
    return render_template('index.jinja', title='Home', events=events)

@app.route('/events', methods= ['POST'])
def add_event():
    event_name = request.form['name']
    event_guests = int(request.form['guests'])
    print(request.form["recurring"])
    if request.form['recurring'] == "True":
        event_recurring = True
    else:
        event_recurring = False
    event_date = request.form['date']
    event_location = request.form['room_location']
    event_description = request.form['description']

    new_event = Event(event_date,event_name,event_guests,event_recurring,event_location,event_description)
    print(new_event)

    add_new_event(new_event)
    return  render_template('index.jinja', title='Home', events=events)

# @app.route('/events/delete/<index>')
#     def delete_item(index):
#         return