# Imports discordpy Package
import discord

# Creates client
client = discord.Client()


@client.event  # Event decorator/wrapper
async def on_ready():
    print(f"HelloBot ready! Logged as... {client.user}")


@client.event
async def on_message(message):  # Checks for every new message
    print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")

    # Sends back a reply when a string has been written by a user.
    if message.content.lower() == 'hi py-chan':
        await message.channel.send('Hello, ' + message.author.mention)


# Login using your token
client.run("USE YOUR OWN TOKEN")
