# Imports discordpy Package
import discord
intents = discord.Intents.all()  # Check docs for intents

# Creates client
client = discord.Client(intents=intents)

newUserMessage = "Insert Message Here"


@client.event  # Event decorator/wrapper
async def on_ready():
    print(f"WelcomeRoleBot ready! Logged as... {client.user}")


@client.event
async def on_member_join(member):
    welcome_channel = client.get_channel()  # Use your own channel ID
    welcome_msg = 'Welcome to the server, ' + member.mention + '👋\n'
    cmd_list = f"```Available commands are: \n!headcount\n!att_report\n!rock\n!paper\n!scissors```\n"
    hi_py = 'Don\'t forget to say "hi py-chan" in any channel!'
    await welcome_channel.send(welcome_msg + cmd_list + hi_py)


# Login using your token
client.run("USE YOUR OWN TOKEN")
