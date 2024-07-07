import date_converter
from datetime import datetime

class event: # object class
  def __init__(self, event_name: str, event_date: str, event_time: str, event_url: str, event_image: str):
    self.event_name = event_name
    self.event_date = event_date
    self.event_time = event_time
    self.event_url = event_url
    self.event_image = event_image

# TODO: Extract event info and pass it to another array (possibly stored as a csv file?)
def populate(events: list, data: dict):
  # populating the array
  for e in data.get('events', []):
    event_name = (
      e.get('name').
      get('text', 'N/A').
      replace(' - Stereo Live Dallas', '')
    )
    
    # if statement makes sure that parking passes "events" don't make it to the final array
    # This is only relevant to Stereo Live, so I don't see It'll Do events jumping to this if statement
    if event_name.startswith('Parking Pass'):
      continue
    event_start_datetime = datetime.fromisoformat(e.get('start').get('local', 'N/A'))
    event_end_datetime = datetime.fromisoformat(e.get('end').get('local', 'N/A'))
    event_date = event_start_datetime.strftime('%B %d, %Y')
    event_start_time = event_start_datetime.strftime('%I:%M %p')
    event_end_time = event_end_datetime.strftime('%I:%M %p')
    event_time = f'{event_start_time} - {event_end_time}'
    event_url = e.get('url', 'N/A')
    event_image = (
      e.get('logo').
      get('original').
      get('url', 'N/A')
    )
    event_object = event(event_name, event_date, event_time, event_url, event_image)
    events.append(event_object)

  return events