from dotenv import load_dotenv
load_dotenv()
import discord
import os

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_member_join(member):
  print('Member joined, sending application')
  if member.dm_channel:
    return

  await member.create_dm() 
  await member.dm_channel.send('IGN:')

#Using this event to test the dm message without new person joining the discord
@client.event
async def on_message(message):
  if message.author.id is client.user.id:
    return
  if message.content.startswith('!porn'):
    await message.author.create_dm()
    await message.author.dm_channel.send('Hey! Welcome to Lasagn :tada:! Please read the rules in the rules channel, and copy paste your application into this bot\'s dms!')

client.run(os.getenv("TOKEN"))