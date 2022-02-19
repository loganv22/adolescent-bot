# some code sourced from https://realpython.com/how-to-make-a-discord-bot-python/
import os
import random
import util as u
from keep_alive import keep_alive

import discord
from dotenv import load_dotenv

# fancy tech stuff - gets the secrets
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# useful variables
prefix = u.textRead("settings.txt")[3]
client = discord.Client()
rps = False

# displays when bot connects
@client.event
async def on_ready():
  print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_message(message):
  global rps
  
  if message.author == client.user:
    return
  if message.content.startswith(prefix + "rps"):
    await message.channel.send("Ok let's play. You go first.")
    rps = True
    return
  if rps:
    if message.content.lower() == "rock":
        await message.channel.send("Paper")
        await message.channel.send("Ha ha! I win!")
        await message.channel.send(u.randomYourMomJoke())
    elif message.content.lower() == "scissors":
        await message.channel.send("Rock")
        await message.channel.send("Ha ha! I win!")
        await message.channel.send(u.randomYourMomJoke())
    elif message.content.lower() == "paper":
        await message.channel.send("Scissors")
        await message.channel.send("Ha ha! I win!")
        await message.channel.send(u.randomYourMomJoke())
    else:
        await message.channel.send("That's not rock, paper, or scissors. I don't play with cheaters.")
    rps = False
    return

  if message.content.startswith(prefix + "insult"):
    insultRequest = message.content.split(" ")
    if len(insultRequest) > 1 and insultRequest[1].startswith("<@"):
      await message.channel.send(u.randomYourMomJoke(insultRequest[1]))
      if random.randrange(100) > 100 - int(u.textRead("settings.txt")[2]):
        await message.channel.send(file=discord.File('insults/roastedgifs/roasted'+str(random.randint(1, 5))+ '.gif'))
    else:
      await message.channel.send(u.randomYourMomJoke())
      if random.randrange(100) > 100 - int(u.textRead("settings.txt")[2]):
        await message.channel.send(file=discord.File('insults/roastedgifs/roasted'+str(random.randint(1, 5))+ '.gif'))
    return
  elif message.content.startswith(prefix + "geninsult"):
    insultRequest = message.content.split(" ")
    if len(insultRequest) > 1 and insultRequest[1].startswith("<@"):
      await message.channel.send(u.generateYourMomJoke(insultRequest[1]))
      if random.randrange(100) > 100 - int(u.textRead("settings.txt")[2]):
        await message.channel.send(file=discord.File('insults/roastedgifs/roasted'+str(random.randint(1, 5))+ '.gif'))
    else:
      await message.channel.send(u.generateYourMomJoke())
      if random.randrange(100) > 100 - int(u.textRead("settings.txt")[2]):
        await message.channel.send(file=discord.File('insults/roastedgifs/roasted'+str(random.randint(1, 5))+ '.gif'))
    return
  elif message.content.startswith(prefix + "help"):
    await message.channel.send(f"""
Hello! I'm a very accurate representation of an annoying adolescent, created by a group of annoying adolescents. I tell the best your mom jokes you've ever encountered. Try some of these commands!

**don't spam commands. we'll get rate limited.**

Command prefix: {prefix}

{prefix}**help**
The help command.

{prefix}**insult** *[optional_target]*
Get a your mom joke. If you ping someone after the command, I'll insult their mom instead of yours.

{prefix}**geninsult** *[optional_target]*
I'll generate a your mom joke instead of choosing one from my premade list as with {prefix} insult. If you ping someone after the command, I'll insult their mom instead of yours.

{prefix}**rps**
We'll play a game of rock paper scissors. You'll definitely be able to win if you try hard enough.

Coming soon: commands for changing the frequency of random responses to messages
Curse another Discord server with my presence!
https://discord.com/api/oauth2/authorize?client_id=944652303632322591&permissions=277025459264&redirect_uri=https%3A%2F%2Fdiscord.com%2Fchannels%2F%40me&response_type=code&scope=bot%20messages.read

*I'm dedicated to ZA!* You know what you said about my mother.

*This is a submission for Hack Kean 2022*
""")
    return
    
  animal = u.containsAny(message.content, u.textRead("insults/animals.txt"))
  if random.randrange(100) > 100 - int(u.textRead("settings.txt")[0]) and animal:
    await message.channel.send(f'{animal.title()}? Like your mom?')
    return
        
  if random.randrange(100) > 100 - int(u.textRead("settings.txt")[1]): 
    if (
      message.content.lower().startswith("who ") or
      message.content.lower().startswith("what ") or
      message.content.lower().startswith("when ") or
      message.content.lower().startswith("where ") or
      message.content.lower().startswith("why ") or
      message.content.lower().startswith("how ") or
      message.content.lower().startswith("do") or
      message.content.lower().startswith("does") or
      message.content.lower().startswith("can") or
      message.content.lower().startswith("has") or
      message.content.lower().startswith("have") or
      message.content.lower().startswith("will ") or
      message.content.lower().startswith("won't ") or
      message.content.lower().startswith("would") or
      message.content.lower().startswith("should") or
      message.content.lower().startswith("could") or
      message.content[-1] == "?"
    ):
      await message.channel.send('your mom LMAO xD')
      return 
    else: 
      await message.channel.send('i literally didn\'t ask')
      return
      
keep_alive() 
client.run(TOKEN)