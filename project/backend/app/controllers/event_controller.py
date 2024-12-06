from flask import Blueprint, request, jsonify
from app.services.event_service import create_event, list_events, get_saludo

event_bp = Blueprint('event', __name__) 

@event_bp.route('/hello', methods=['GET']) 
def saludo():
    result = get_saludo()
    return jsonify(result)


@event_bp.route('/', methods=['GET']) 
def get_events(): 
    return "List of events"



@event_bp.route('event', methods=['POST'])
def create():
    data = request.get_json()
    event_date = datetime.strptime(data['date'], '%Y-%m-%d %H:%M:%S')
    event = create_event(data['title'], data['description'], data['date'], data['location'], data['user_id'])
    return jsonify({'message': 'Event created successfully!', 'event': event.id}), 201

@event_bp.route('/events', methods=['GET'])
def get_all():
    events = list_events()
    return jsonify([{'id': event.id, 'title': event.title, 'description': event.description, 'date': event.date, 'location': event.location, 'user_id': event.user_id} for event in events]), 200
