# Created by Zaki :)
import discord
import PIL
from discord.ext import commands
from NyaaPy import Nyaa
import random
import asyncio
intents = discord.Intents(messages=True, guilds=True, invites=True, bans=True, members=True, dm_messages=True, reactions=True, guild_reactions=True)

bot = commands.Bot(command_prefix=commands.when_mentioned_or("$"),
                   description='Lain bot by Zaki', case_insensitive=True, intents=intents)


bot.remove_command('help')

@bot.command()
@commands.is_owner()
async def load(ctx, extension):
    await ctx.send(f"Załadowano {extension}")
    bot.load_extension(f'cogs.{extension}')


@bot.command()
@commands.is_owner()
async def unload(ctx, extension):
    await ctx.send(f"Rozładowano {extension}")
    bot.unload_extension(f'cogs.{extension}')


@bot.command()
@commands.is_owner()
async def rload(ctx, extension):
    await ctx.send(f"Przeładowano {extension}")
    bot.unload_extension(f'cogs.{extension}')
    bot.load_extension(f'cogs.{extension}')
@bot.command()
@commands.is_owner()
async def rall(ctx):
    bot.unload_extension(f'cogs.fun')
    bot.unload_extension(f'cogs.utility')
    bot.unload_extension(f'cogs.reaction')
    bot.unload_extension(f'cogs.moderation')
    #bot.unload_extension(f'cogs.economy')
    bot.load_extension(f'cogs.fun')
    bot.load_extension(f'cogs.utility')
    bot.load_extension(f'cogs.reaction')
    bot.load_extension(f'cogs.moderation')
    #bot.load_extension(f'cogs.economy')
    await ctx.send(f"Przeładowano wszystko")

@bot.command()
async def anime(ctx, *, message):#Searches for anime torrents from Nyaa wrapper
    dict = Nyaa.search(keyword=message, category=1)
    name = dict[0]['name']
    size = dict[0]['size']
    seeders = dict[0]['seeders']
    download = dict[0]['download_url']
    await ctx.send("Nazwa: "+name+" Rozmiar:"+size+" Seeders:"+seeders+" Link: "+download)


@bot.event
async def on_ready():
    print('Logged in as {0} ({0.id})'.format(bot.user))
    print('------')
    status = "$help | Version 0.2"
    await bot.change_presence( activity=discord.Game(name=status))


bot.load_extension(f'cogs.fun')
bot.load_extension(f'cogs.utility')
bot.load_extension(f'cogs.reaction')
bot.load_extension(f'cogs.moderation')
#bot.load_extension(f'cogs.economy')
bot.run('TOKEN')
