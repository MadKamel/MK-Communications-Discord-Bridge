# ( ͡° ͜ʖ ͡°)
import discord, os, irc, comms, threading
os.system('clear')


channel = "#mk-comms"
server = "irc.freenode.net"
nickname = "mk-2-dis"

ircclient = irc.IRC()
ircclient.connect(server, channel, nickname, "MK-COMMS Test Service")

intents = discord.Intents.all()
token = os.getenv('token')
client = discord.Client(intents=intents)

def ircDaemon():
  while True:
    cmd, user, fullmsg = comms.parsecmd(ircclient.get_text())
    if not cmd == None:
      if cmd == 'ping':
        client.send('pong')
        print('ping from ' + user + ' ponged.')
    
      elif cmd == 'pong':
        print('pong from ' + user + ' recieved.')

      elif cmd == 'send':
        if fullmsg.split(' ')[1] == nickname:
          sent_command = ' '.join(fullmsg.split(' ')[2:])
          print('sending message from ' + user + ' to logs.')
          print(sent_command)



@client.event
async def on_message(msg):
  ircclient.send(msg.content)


ircDaemonProc = threading.Thread(target=ircDaemon, daemon=True)
ircDaemonProc.start()


print('MK-COMMS bridge going online.')
client.run(token)
