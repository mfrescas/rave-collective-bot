import os
from discord import Client, Intents, Message, Embed
from random import choice
import api
import event
import venue_list

# Set-Up
TOKEN = os.environ['DISCORD_TOKEN']
intents: Intents = Intents.default()
intents.message_content = True
client: Client = Client(intents=intents)

# Start-Up
@client.event
async def on_ready() -> None:
  print(f'{client.user} is ready to rumble!')

@client.event
async def on_message(message: Message) -> None:
  if message.author == client.user:
    return
  username: str = str(message.author)
  user_message: str = str(message.content)
  channel: str = str(message.channel)
  print(f'{username} said: "{user_message}" ({channel})')
  await send_message(message, user_message)

# This is where the magic happens (where you put your code)
def get_response(user_input: str) -> str:
  lowered: str = user_input.lower()

  if 'tonight' in lowered:
    return '<@&1232355460674355260>'
  else:
    return "Please type \"tonight\" to return the embed."

async def send_message(message: Message, user_message: str) -> None:
  if not user_message:
    print('Message was empty because intents were not enabled propbably')
    return
  try:
    response: str = get_response(user_message)
    if response[1].__contains__('@'):
      # Stereo Live Dallas Venue ID: 56848259
      # It'll Do Venue ID: 43512991

      data = api.request(56848259)
      
      events: tuple = tuple(event.populate([], data))
      embed = Embed(
        title = events[0].event_name, 
        url = events[0].event_url, 
        description = (events[1].event_date + ' | ' + events[0].event_time),
        color = 0xff0000
      )
      embed.set_image(url = events[0].event_image)
      await message.channel.send(response, embed=embed)
    else:
      await message.channel.send(response)
  except Exception as e:
    print(e)

def main() -> None:
  client.run(token=TOKEN)
  
  if __name__ == '__main__':
    main()