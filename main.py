#python discord bot
#bot.py
#code made by upsettingcord
#Version 1 not currently for discord due to possible ToS
import discord
from discord.ext import commands, tasks
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")

client = discord.Client()
client = commands.Bot("$", self_bot = True)

@client.event
async def on_ready():
    print('Client has connected')
    for guild in client.guilds:
        if guild.name == GUILD:
             break

 print(
        f'{client.user} is connected to the following guild:\n'
        f'{GUILD.name}(id: {GUILD.id})'
    )

client.run(TOKEN)

