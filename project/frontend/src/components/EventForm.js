import React, { useState } from 'react';
import { createEvent } from '../services/eventService';

const EventForm = () => {
  const [title, setTitle] = useState('');
  const [date, setDate] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    await createEvent({ title, date });
    // Reset form or handle success
  };

  return (
    <form onSubmit={handleSubmit}>
      <input type="text" placeholder="Event Title" value={title} onChange={(e) => setTitle(e.target.value)} required />
      <input type="datetime-local" value={date} onChange={(e) => setDate(e.target.value)} required />
      <button type="submit">Create Event</button>
    </form>
  );
};

export default EventForm;