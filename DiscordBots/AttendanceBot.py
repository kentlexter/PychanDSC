# Imports discordpy Package
import discord
intents = discord.Intents.all()  # Check docs for intents

# Creates client
client = discord.Client(intents=intents)


@client.event  # Event decorator/wrapper
async def on_ready():
    print(f"AttedanceBot ready! Logged as... {client.user}")


@client.event
async def on_message(message):  # Checks for every new message
    print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")

    # Gets "guild" number of your Discord Server
    # Replace this
    # INSERT YOUR OWN GUILD NUMBER AKA Discord Server ID)
    py_guild = client.get_guild()

    if message.content.lower() == "!headcount":  # Checks number of guild members
        await message.channel.send(f"```py\n{py_guild.member_count}```")
    elif message.content.lower() == "!att_report":  # Checks status of guild members
        online = 0
        offline = 0     # Refer to discord.Status in the docs
        idle = 0
        dnd = 0
        for m in py_guild.members:
            if str(m.status) == "online":
                online += 1
            elif str(m.status) == "idle":
                idle += 1
            elif str(m.status) == "dnd":
                dnd += 1
            elif str(m.status) == "offline":
                offline += 1
    await message.channel.send(f"```Online: {online}\nIdle: {idle}\nDo Not Disturb: {dnd}\nOffline: {offline}```")

# Login using your token
client.run("USE YOUR OWN TOKEN")
