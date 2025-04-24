import React, { useEffect, useState } from 'react';
import { getEvents } from '../services/eventService';

const EventList = () => {
  const [events, setEvents] = useState([]);

  useEffect(() => {
    const fetchEvents = async () => {
      const data = await getEvents();
      console.log (data)
      setEvents(data);
    };
    fetchEvents();
  }, []);

  return (
    <div>
      <h2>Event List</h2>
      <ul>
        {Array.isArray(events) && events.map(event => ( <li key={event.id}>{event.title} - {event.date}</li> ))}
      </ul>
    </div>
  );
};

export default EventList;