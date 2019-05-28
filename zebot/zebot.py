import discord
from discord.ext import commands
import config

bot = commands.Bot(command_prefix=config.prefix)


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command()
async def ping(ctx):
    await ctx.send('pong')

bot.run(config.token_secret)
