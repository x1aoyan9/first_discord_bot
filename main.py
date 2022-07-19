# https://youtu.be/SPTfmiYiuok
import discord
import os
import requests
import json
import random
from replit import db
from keep_alive import keep_alive
from sad_words import sad_words
# import help_command

client = discord.Client()

welcoming = ["hi mode","Hi Mode","hey mode","Hey Mode","sup mode","Sup Mode","hello mode","Hello Mode","Mode?", "mode?"]

resp_welc = ["Hey", "Hello", "...booting up...", "Mode is sleepy...zzz","Hi","Zzz","^^"]

starter_encouragements = [
  "Cheer up!",
  "Hang in there!",
  "You are a great person/bot!"
]

if "responding" not in db.keys():
  db["responding"] = True

intents = discord.Intents().all() #Enable all intents (same as Admin permissions)

# request inspirational quote from the API
def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + "  - " + json_data[0]['a']
  return(quote)

def update_encouragements(encouraging_message):
  if "encouragements" in db.keys():
    encouragements = db["encouragements"]
    encouragements.append(encouraging_message)
    db["encouragements"] = encouragements
  else:
    db["encouragements"] = [encouraging_message]

def delete_encouragement(index):
  encouragements = db["encouragements"]
  if len(encouragements) > index:
    del encouragements[index]
    db["encouragements"] = encouragements

# prints in the console that the bot has been successfully activated
@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

# prevents the bot from responding to itself(?)
@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  # Mode says Hello to whoever sends the command
  if msg.startswith('$hello'):
    await message.channel.send('Hello!')

  # Mode's introduction
  if msg.startswith('$selfintroduction'):
    await message.channel.send("...processing pre-recorded message... Hey! I'm Mode! Your friendly office place robot! You can pay me in compliments and carrot oil!")
  
  if msg.startswith('$inspire'):
    quote = get_quote()
    await message.channel.send(quote)

  if db["responding"]:
    options = starter_encouragements
  
    if "encouragements" in db.keys():
      options = options + db["encouragements"].value

    # responds to the use of the dict of sad_words
    if any(word in msg for word in sad_words):
      await message.channel.send(random.choice(options))

    # responds to the use of dict of welcoming
    if any(word in msg for word in welcoming):
      await message.channel.send(random.choice(resp_welc))

  # add a new message of encouragement
  if msg.startswith('$new'):
    encouraging_message = msg.split('$new ',1)[1]
    update_encouragements(encouraging_message)
    await message.channel.send("New encouraging message added.")

  # delete a message of encouragement(via their index num)
  if msg.startswith('$del'):
    encouragements = []
    if "encouragements" in db.keys():
      index = int(msg.split('$del',1)[1])
      delete_encouragement(index)
      encouragements = db["encouragements"]
    await message.channel.send(encouragements)

  # if msg.startswith('$help'):
  #   await message.channel.send('')

  #lists the db of encouragements 
  if msg.startswith('$list'):
    encouragements = []
    if "encouragements" in db.keys():
      encouragements = db["encouragements"]
    await message.channel.send(encouragements)

  # switch to turn on/off the bot responding to commands
  if msg.startswith('$responding'):
    value = msg.split('$responding ',1)[1]
    
    if value.lower() == "true":
      db['responding'] = True
      await message.channel.send("Responding is on.")
    else:
      db['responding'] = False
      await message.channel.send("Responding is off.")

# keeps the bot active(when it's being pinned)
keep_alive()
client.run(os.environ['TOKEN'])
