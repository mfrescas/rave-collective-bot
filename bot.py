import os
from discord import Client, Intents, Embed
import api
import event
from venue_list import venue_list
from datetime import datetime
import asyncio

# Set-Up
TOKEN = os.environ['DISCORD_TOKEN']
intents: Intents = Intents.default()
intents.message_content = True
client: Client = Client(intents=intents)

# Event Data for different venues
# Please check venue_list.py for each venue's index
venue_data: list = []
for venue in venue_list:
  # Access Venue ID from each venue on venue_list.py and populate venue_data accordingly
  venue_data.append(api.request(venue_list[venue][0]))

events: tuple = tuple(
    event.populate([], venue_data[0])
)  # You can change the index in venue_data to access events for different venues


# Start-Up
@client.event
async def on_ready() -> None:
  print(f'{client.user} is ready to rumble!')
  await is_there_event_today()  


# This is where the magic happens (where you put your code)
@client.event
async def is_there_event_today():
  while True:
    for event in events:
      # You can add logic here to check if the event is today
      if event.event_date == datetime.now().strftime('%B %d, %Y'):
        # create embed
        embed = Embed(
          title = events[0].event_name, 
          url = events[0].event_url, 
          description = (events[0].event_date + ' | ' + events[0].event_time),
          color = int(venue_list['Stereo-Live-Dallas'][2], 16)
        )
        embed.set_image(url = events[0].event_image)
        embed.set_author(
          name = 'TONIGHT @ STEREO LIVE DALLAS', 
          icon_url = venue_list['Stereo-Live-Dallas'][3])
        await client.get_channel(1232195766492336243).send(f'<@&1232355460674355260>', embed=embed)
    await asyncio.sleep(3600) # sleep is measured in seconds (i think), 3600 seconds = 1 hour 

def main() -> None:
  client.run(token=TOKEN)

  if __name__ == '__main__':
    main()
