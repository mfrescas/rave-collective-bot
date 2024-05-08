import os
from urllib.request import Request, urlopen
import json

KEY = os.environ['API_KEY']
headers = {
  'Authorization': f'Bearer {KEY}'
}

def request(venue_id: int):
  # TODO: Have an integer that will choose to get a request frmo either SL or It'll do
  request = Request(
    f'https://www.eventbriteapi.com/v3/venues/{venue_id}/events/?status=live&order_by=start_asc&only_public=True&token={KEY}', headers=headers
  )
  
  response_body = urlopen(request).read()

  # Extracting specific fields from the API response
  data = json.loads(response_body)

  return data