import discord
from discord.ext import commands
import asyncio
import sqlite3

bot = commands.Bot(command_prefix='~')

@bot.event
@asyncio.coroutine
def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command()
@asyncio.coroutine
def parrot(*, message: str):
    yield from bot.say(message)


bot.run('')
