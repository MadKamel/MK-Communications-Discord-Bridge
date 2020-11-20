# ( ͡° ͜ʖ ͡°)
import discord, os
os.system('clear')

intents = discord.Intents.all()
token = os.getenv('token')
client = discord.Client(intents=intents)



@client.event
async def on_message(msg):
  print(msg.content)



print('KamelBot going online.')
client.run(token)
