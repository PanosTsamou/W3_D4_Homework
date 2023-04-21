from models.event import *
import datetime



event1 = Event(datetime.date.today(), "Staff Meeting", 35,  True, 'EDI1', "All staff meeting")
event2 = Event(datetime.date(2023, 4, 21) , "1-1 review", 2,  False, 'GLA3', "1-1 Review for weekend Homework")
event3 = Event(datetime.date(2023, 4, 22) , "Quiz Night", 40,  False, 'Open Area', "Quiz night for all cohorts")

events = [event1, event2, event3]


def add_new_event(event):
    events.append(event)

