from app.models.event import Event
from datetime import datetime

def add_event(event):
    db.session.add(event)
    db.sessio.commit()
        
def det_all_events():
    return Event.query.all()

     
def eventsVigentes (dateref):
    return Event.query.filter(Event.date>=dateref).all()
