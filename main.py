import discord
import os


intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_member_join(member):
 # APPLICANT_TABLE[member.id].append(APPLICANT_DATA)
  print('Member joined, sending application')
  if member.dm_channel:
    return

  await member.create_dm() 
  await member.dm_channel.send('IGN:')
  


client.run(os.getenv('TOKEN'))