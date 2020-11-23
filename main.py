# ( ͡° ͜ʖ ͡°)
import discord, os, irc
os.system('clear')


channel = "#mk-comms"
server = "irc.freenode.net"
nickname = "mk-2-dis"

ircclient = irc.IRC()
ircclient.connect(server, channel, nickname, "MK-COMMS Test Service")

intents = discord.Intents.all()
token = os.getenv('token')
client = discord.Client(intents=intents)



@client.event
async def on_message(msg):
  ircclient.send(msg.content)



print('MK-COMMS bridge going online.')
client.run(token)
