import discord
import asyncio
from config import cfg

cli = discord.Client()

@cli.event
async def on_ready():
    print("Hello there !")

@cli.event
async def on_message(message):
    if (message.author.id != cfg.id):
        print(message.author.name + ": " + message.content)
        await message.channel.send("Bien reçu")

@cli.event
async def on_reaction_add(reaction, user):
    print("ui")