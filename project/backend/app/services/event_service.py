from app.repositories.event_repository import add_event, get_all_events
from app.models.event import Event

def create_event(title, description, date, location, user_id):
    new_event = Event(title=title, description=description, date=date, location=location, user_id=user_id)
    add_event(new_event)
    return new_event

def list_events():
    return get_all_events()

def get_saludo():
    data = {"message": "Hola mundo"}
    return data
