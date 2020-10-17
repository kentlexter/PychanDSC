# Imports discordpy Package
import discord
import random

# Creates client
client = discord.Client()


@client.event  # Event decorator/wrapper
async def on_ready():
    print(f"RPSBotv2 ready! Logged as... {client.user}")


@client.event
async def on_message(message):  # Checks for every new message
    usr_play = message.content.lower()
    win_cases = [["rock", "scissors"], [
        "scissors", "paper"], ["paper", "rock"]]
    game_opt = ["!rock", "!paper", "!scissors"]
    rps_pic = {"rock": "✊", "paper": "🖐", "scissors": "✌"}
    bot_play = random.randint(0, 2)

    if usr_play in game_opt:
        usr_picks = usr_play[1:]
        bot_picks = game_opt[bot_play][1:]
        game_stat = message.author.mention + ' picked ' + \
            rps_pic[usr_picks] + ' against my ' + rps_pic[bot_picks]
        if usr_picks == bot_picks:
            await message.channel.send('DRAW! - ' + game_stat)
        elif ([usr_picks, bot_picks] in win_cases):
            await message.channel.send('You WIN! - ' + game_stat)
        else:
            await message.channel.send('You LOSE!- ' + game_stat)


# Login using your token
client.run("USE YOUR OWN TOKEN")
