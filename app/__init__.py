import discord
import asyncio
import youtube_dl
from discord.ext.commands import Bot
from config import cfg

cli = Bot(cfg.prefix)

@cli.event
async def on_ready():
    print("Hello there !")

@cli.command()
async def join(ctx):
    channel = ctx.author.voice.channel

    await channel.connect()

@cli.command()
async def play(ctx, url: str):
    voice_cli = ctx.guild.voice_client
    voice_cli.play(discord.FFmpegPCMAudio("sound.mp3"))
