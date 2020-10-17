# Imports discordpy module
import discord
import math
import random

# Creates client
client = discord.Client()


@client.event  # Event decorator/wrapper
async def on_ready():
    print(f"RPSBot ready! Logged as... {client.user}")


@client.event
async def on_message(message):  # Checks for every new message
    chosenArray = [" picked ✊ ",
                   "  picked 🖐 ", " picked ✌"]
    gameOptions = ["✊", "🖐", "✌"]
    winMsg = [". It is a draw", ". You lose", ". You win!"]
    # Generates number between 0 and 2 (both included)
    ranNum = random.randint(0, 2)
    botPlay = gameOptions[ranNum]

    # If user picks Rock
    if message.content.lower() == '!rock':

        if botPlay == gameOptions[0]:  # rock vs rock (tie)
            await message.channel.send(message.author.mention + chosenArray[0]
                                       + 'against my ' + botPlay + winMsg[0])
        elif botPlay == gameOptions[1]:  # rock vs paper (lose)
            await message.channel.send(message.author.mention + chosenArray[0]
                                       + 'against my ' + botPlay + winMsg[1])
        elif botPlay == gameOptions[2]:  # rock vs scissors (win)
            await message.channel.send(message.author.mention + chosenArray[0]
                                       + 'against my ' + botPlay + winMsg[2])

    # If user picks Paper
    if message.content.lower() == '!paper':

        if botPlay == gameOptions[0]:  # paper vs rock (win)
            await message.channel.send(message.author.mention + chosenArray[1]
                                       + 'against my ' + botPlay + winMsg[2])
        elif botPlay == gameOptions[1]:  # paper vs paper (draw)
            await message.channel.send(message.author.mention + chosenArray[1]
                                       + 'against my ' + botPlay + winMsg[0])
        elif botPlay == gameOptions[2]:  # paper vs scissors (lose)
            await message.channel.send(message.author.mention + chosenArray[1]
                                       + 'against my ' + botPlay + winMsg[1])

    # If user picks Scissors
    if message.content.lower() == '!scissors':

        if botPlay == gameOptions[0]:  # scissors vs rock (lose)
            await message.channel.send(message.author.mention + chosenArray[2]
                                       + 'against my ' + botPlay + winMsg[1])
        elif botPlay == gameOptions[1]:  # scissors vs paper (win)
            await message.channel.send(message.author.mention + chosenArray[2]
                                       + 'against my ' + botPlay + winMsg[2])
        elif botPlay == gameOptions[2]:  # scissors vs scissors (draw)
            await message.channel.send(message.author.mention + chosenArray[2]
                                       + 'against my ' + botPlay + winMsg[0])


# Login using your token
client.run("USE YOUR OWN TOKEN")
