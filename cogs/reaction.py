import discord
import io
import aiohttp
import nekos
import requests
import json
import random
from discord.ext import commands

import TenGiphPy

t = TenGiphPy.Tenor(token="C9Z95CRF4TYD")
apikey = "C9Z95CRF4TYD"
lmt = 1
search = "anime"
class Reaction(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #Events
    @commands.Cog.listener()
    async def on_ready(self):
        print("Cog Reaction is ready")
    
    
    #Emotes
    @commands.command()
    async def baka(self, ctx):
        msg = f"B-Baka!"
        embed = discord.Embed(description=msg, color=0x000033)
        embed.set_image(url=nekos.img("baka"))
        await ctx.send(embed=embed)
    

    @commands.command()
    async def tenor(self, ctx, *, giftag):
        getgifurl = t.random(str(giftag))
        await ctx.send(f'{getgifurl}')


    @commands.command()
    async def drink(self, ctx):
        author = ctx.author
        getgifurl = t.random("anime drink")
        msg = f"{author.mention} pije"
        embed = discord.Embed(description=msg, color=0x000033)
        embed.set_image(url=getgifurl)
        await ctx.send(embed=embed)


    @commands.command()
    async def facepalm(self, ctx):
        author = ctx.author
        getgifurl = t.random("anime facepalm")
        msg = f"Co..."
        embed = discord.Embed(description=msg, color=0x000033)
        embed.set_image(url=getgifurl)
        await ctx.send(embed=embed)


    @commands.command()
    async def confused(self, ctx):
        author = ctx.author
        getgifurl = t.random("anime confused")
        msg = f"{author.mention} jest zdezorientowany"
        embed = discord.Embed(description=msg, color=0x000033)
        embed.set_image(url=getgifurl)
        await ctx.send(embed=embed)


    @commands.command()
    async def facedesk(self, ctx):
        author = ctx.author
        getgifurl = t.random("anime facedesk")
        msg = f""
        embed = discord.Embed(description=msg, color=0x000033)
        embed.set_image(url=getgifurl)
        await ctx.send(embed=embed)


    @commands.command()
    async def angry(self, ctx):
        author = ctx.author
        getgifurl = t.random("anime angry")
        msg = f"{author.mention} jest zły"
        embed = discord.Embed(description=msg, color=0x000033)
        embed.set_image(url=getgifurl)
        await ctx.send(embed=embed)


    @commands.command()
    async def thumbsup(self, ctx):
        author = ctx.author
        getgifurl = t.random("anime thumbsup")
        msg = f"👍"
        embed = discord.Embed(description=msg, color=0x000033)
        embed.set_image(url=getgifurl)
        await ctx.send(embed=embed)


    @commands.command()
    async def pout(self, ctx):
        author = ctx.author
        getgifurl = t.random("anime pout")
        msg = f"{author.mention} pouts"
        embed = discord.Embed(description=msg, color=0x000033)
        embed.set_image(url=getgifurl)
        await ctx.send(embed=embed)


    @commands.command()
    async def blush(self, ctx):
        author = ctx.author
        getgifurl = t.random("anime blush")
        msg = f"{author.mention} się rumieni!"
        embed = discord.Embed(description=msg, color=0x000033)
        embed.set_image(url=getgifurl)
        await ctx.send(embed=embed)


    @commands.command()
    async def sleepy(self, ctx):
        author = ctx.author
        getgifurl = t.random("anime sleepy")
        msg = f"{author.mention} jest śpiący 😴..."
        embed = discord.Embed(description=msg, color=0x000033)
        embed.set_image(url=getgifurl)
        await ctx.send(embed=embed)


    @commands.command()
    async def dance(self, ctx):
        author = ctx.author
        getgifurl = t.random("anime dance")
        msg = f"{author.mention} tańczy"
        embed = discord.Embed(description=msg, color=0x000033)
        embed.set_image(url=getgifurl)
        await ctx.send(embed=embed)
    

    @commands.command()
    async def think(self, ctx):
        getgifurl = t.random("anime think")
        msg = f"Hmmm...."
        embed = discord.Embed(description=msg, color=0x000033)
        embed.set_image(url=getgifurl)
        await ctx.send(embed=embed)


    @commands.command()
    async def happy(self, ctx):
        author = ctx.author
        getgifurl = t.random("anime happy")
        msg = f"{author.mention} jest szczęśliwy!"
        embed = discord.Embed(description=msg, color=0x000033)
        embed.set_image(url=getgifurl)
        await ctx.send(embed=embed)


    @commands.command()
    async def grin(self, ctx):
        getgifurl = t.random("anime grin")
        msg = f"Tee heee..."
        embed = discord.Embed(description=msg, color=0x000033)
        embed.set_image(url=getgifurl)
        await ctx.send(embed=embed)


    @commands.command()
    async def cool(self, ctx):
        getgifurl = t.random("anime sunglasses")
        msg = f"😎"
        embed = discord.Embed(description=msg, color=0x000033)
        embed.set_image(url=getgifurl)
        await ctx.send(embed=embed)


    @commands.command()
    async def shrug(self, ctx):
        author = ctx.author
        getgifurl = t.random("anime shrug")
        msg = f"{author.mention} wzrusza ramionami"
        embed = discord.Embed(description=msg, color=0x000033)
        embed.set_image(url=getgifurl)
        await ctx.send(embed=embed)


    @commands.command()
    async def initiald(self, ctx):
        author = ctx.author
        getgifurl = t.random("anime initiald")
        msg = f"EUROBEAT INTENSIFITES"
        embed = discord.Embed(description=msg, color=0x000033)
        embed.set_image(url=getgifurl)
        await ctx.send(embed=embed)


    @commands.command()
    async def smug(self, ctx):
        response = requests.get("http://api.nekos.fun:8080/api/smug")
        author = ctx.message.author.mention
        data = response.json()
        msg = f"{author} smugs"
        embed = discord.Embed(description=msg, color=0x000033)
        embed.set_image(url=data["image"])
        await ctx.send(embed=embed)
    
    
    @commands.command()
    async def cry(self, ctx):
        response = requests.get("http://api.nekos.fun:8080/api/cry")
        author = ctx.message.author.mention
        data = response.json()
        msg = f"{author} płacze..."
        embed = discord.Embed(description=msg, color=0x000033)
        embed.set_image(url=data["image"])
        await ctx.send(embed=embed)
    #Actions

    @commands.command()
    async def kill(self, ctx, member: discord.Member):
        author = ctx.author
        getgifurl = t.random("anime kill")
        msg = f"{author.mention} chce zabić {member.mention}"
        embed = discord.Embed(description=msg, color=0x000033)
        embed.set_image(url=getgifurl)
        await ctx.send(embed=embed)


    @commands.command()
    async def handhold(self, ctx, member: discord.Member):
        author = ctx.author
        getgifurl = t.random("handholding anime")
        msg = f"{author.mention} trzyma za ręce {member.mention} 💗"
        embed = discord.Embed(description=msg, color=0x000033)
        embed.set_image(url=getgifurl)
        await ctx.send(embed=embed)


    @commands.command()
    async def highfive(self, ctx, member: discord.Member):
        author = ctx.author
        getgifurl = t.random("anime highfive")
        msg = f"{author.mention} przybija piątke z {member.mention}"
        embed = discord.Embed(description=msg, color=0x000033)
        embed.set_image(url=getgifurl)
        await ctx.send(embed=embed)


    @commands.command()
    async def bite(self, ctx, member: discord.Member):
        author = ctx.author
        getgifurl = t.random("anime bite")
        msg = f"{author.mention} gryzie {member.mention}"
        embed = discord.Embed(description=msg, color=0x000033)
        embed.set_image(url=getgifurl)
        await ctx.send(embed=embed)


    @commands.command()
    async def wave(self, ctx, member: discord.Member):
        author = ctx.author
        getgifurl = t.random("anime bite")
        msg = f"{author.mention} macha w stronę {member.mention}!"
        embed = discord.Embed(description=msg, color=0x000033)
        embed.set_image(url=getgifurl)
        await ctx.send(embed=embed)


    @commands.command()
    async def marry(self, ctx, member: discord.Member):
        author = ctx.author
        getgifurl = t.random("anime marry")
        msg = f"{author.mention} żeni się z {member.mention} 💘"
        embed = discord.Embed(description=msg, color=0x000033)
        embed.set_image(url=getgifurl)
        await ctx.send(embed=embed)


    @commands.command()
    async def choke(self, ctx, member: discord.Member):
        author = ctx.author
        getgifurl = t.random("anime choke")
        msg = f"{author.mention} dusi {member.mention}"
        embed = discord.Embed(description=msg, color=0x000033)
        embed.set_image(url=getgifurl)
        await ctx.send(embed=embed)


    @commands.command()
    async def hug(self, ctx, member: discord.Member):
        if member == None:
            member = ctx.author
        response = requests.get("http://api.nekos.fun:8080/api/hug")
        data = response.json()
        author = ctx.message.author.mention
        msg = f"{author} tuli się z {member.mention} słodko!💜"
        if member == None or member == ctx.author:
            msg = f"Przykro widzieć cię samego chodź tuli!💜"
        embed = discord.Embed(description=msg, color=0x000033)
        embed.set_image(url=data["image"])
        await ctx.send(embed=embed)


    @commands.command()
    async def kiss(self, ctx, member: discord.Member):
        if member == None:
            member = ctx.author
        response = requests.get("http://api.nekos.fun:8080/api/kiss")
        data = response.json()
        author = ctx.message.author.mention
        msg = f"{author} całuje {member.mention} 😳"
        if member == None or member == ctx.author:
            msg = f"Hej czemu jesteś sam? Łap buziaka💛"
        embed = discord.Embed(description=msg, color=0x000033)
        embed.set_image(url=data["image"])
        await ctx.send(embed=embed)

    @commands.command()
    async def slap(self, ctx, member: discord.Member):
        response = requests.get("http://api.nekos.fun:8080/api/slap")
        data = response.json()
        author = ctx.message.author.mention
        msg = f"{author} spoliczkował/a {member.mention}!"
        embed = discord.Embed(description=msg, color=0x000033)
        embed.set_image(url=data["image"])
        await ctx.send(embed=embed)


    @commands.command()
    async def feed(self, ctx, member: discord.Member):
        author = ctx.message.author.mention
        msg = f"{author} karmi {member.mention} ale słodko!<3"
        embed = discord.Embed(description=msg, color=0x000033)
        embed.set_image(url=nekos.img("feed"))
        await ctx.send(embed=embed)


    @commands.command()
    async def cuddle(self, ctx, member: discord.Member):
        author = ctx.message.author.mention
        msg = f"{author} tuli się z {member.mention} słodziutko!<3"
        if member == None or member == ctx.author:
            msg = f"Przykro widzieć cię samego chodź tuli!💜"
        embed = discord.Embed(description=msg, color=0x000033)
        embed.set_image(url=nekos.img("cuddle"))
        await ctx.send(embed=embed)


    @commands.command()
    async def tickle(self, ctx, member: discord.Member):
        author = ctx.message.author.mention
        msg = f"{author} łaskocze {member.mention}!"
        embed = discord.Embed(description=msg, color=0x000033)
        embed.set_image(url=nekos.img("tickle"))
        await ctx.send(embed=embed)


    @commands.command()
    async def poke(self, ctx, member: discord.Member):
        author = ctx.message.author.mention
        msg = f"{author} szturcha {member.mention}"
        embed = discord.Embed(description=msg, color=0x000033)
        embed.set_image(url=nekos.img("poke"))
        await ctx.send(embed=embed)


    @commands.command()
    async def pat(self, ctx, member: discord.Member):
        response = requests.get("http://api.nekos.fun:8080/api/pat")
        author = ctx.message.author.mention
        data = response.json()
        msg = f"{author} głaszcze {member.mention}"
        if member == None or member == ctx.author:
            msg = f"Wydajesz się samotny... chodź pogłaszczę cię!"
        embed = discord.Embed(description=msg, color=0x000033)
        embed.set_image(url=data["image"])
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Reaction(bot))
