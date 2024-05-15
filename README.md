# Hello!
This repository should contain everything that you need to run the bot on your IDE. Just make sure no one else is testing it beforehand :)

# How to test & run the bot
1. Call main() from bot.py
Right now, you can test the bot by sending "tonight" to the server

# Things to do (in order of priority)
- The bot should be able to detect if the current date conatains an event, and send a message about said event, without the need of user input
- Add the capability to handle different local venues
  - Right now we're working on implementing It'll Do. Its venue ID for API calls can be found in venue_list.py
  - It'd preferrable if these venues use EventBrite since there's a general implementation for venues that use that service already 
- If two events at different venues happen at the same date, it should send one message per venue
  - It's impossible for two events to happen at the same venue on the same day (so far)
- Store event list for venues in their individual .csv files
  - This can be used to reduce the amount of API calls that are done everytime the bot turns on
- Optimize
  - Please.
