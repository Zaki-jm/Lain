import discord
import io
import aiohttp
import nekos
import requests
import random
from discord.ext import commands

from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    #Events
    @commands.Cog.listener()
    async def on_ready(self):
        print("Cog Fun is ready")
    
    #Commands
    @commands.command()
    async def repeat(self, ctx, *, msg):
        await ctx.send(msg)
    

    @commands.command()
    async def gay(self, ctx, member: discord.Member):
        if member == None:
            member = ctx.author
        session = aiohttp.ClientSession()
        async with session.get(
                f"https://some-random-api.ml/canvas/gay?avatar={member.avatar_url_as(format='jpg')}") as r:
            if r.status != 200:
                return await ctx.send("**Unable to load image**")
            else:
                data = io.BytesIO(await r.read())
                await ctx.send(file=discord.File(data, 'gay.jpg'))
                await session.close()
    
    @commands.command()
    async def wasted(self, ctx, member: discord.Member):
        if member == None:
            member = ctx.author
        session = aiohttp.ClientSession()
        async with session.get(
                f"https://some-random-api.ml/canvas/wasted?avatar={member.avatar_url_as(format='jpg')}") as r:
            if r.status != 200:
                return await ctx.send("**Unable to load image**")
            else:
                data = io.BytesIO(await r.read())
                await ctx.send(file=discord.File(data, 'wasted.jpg'))
                await session.close()
    
    @commands.command()
    async def triggered(self, ctx, member: discord.Member):
        if member == None:
            member = ctx.author
        session = aiohttp.ClientSession()
        async with session.get(
                f"https://some-random-api.ml/canvas/triggered?avatar={member.avatar_url_as(format='jpg')}") as r:
            if r.status != 200:
                return await ctx.send("**Unable to load image**")
            else:
                data = io.BytesIO(await r.read())
                await ctx.send(file=discord.File(data, 'triggered.jpg'))
                await session.close()


    @commands.command()
    async def waifumeter(self, ctx, member: discord.Member):
        if member == None:
            member = ctx.author
        value = random.randint(0, 100)
        embed = discord.Embed(color=0x000033)
        embed.description = f"{member.mention} jest w " + str(value) + "% super waifu"
        await ctx.send(embed=embed)
    
    @commands.command(aliases=['8ball'])
    async def _8ball(self, ctx, *, question):
        responses = ['Zdecydowanie!.',
                'Bez grama wątpliwości.',
                'Tak - zdecydowanie.',
                'To pewne.',
                'Z tego co wiem, tak.',
                'Prawdopodobnie.',
                'Tak.',
                'Nie pytaj mnie o to teraz.',
                'Lepiej nie wiedzieć.',
                'Nie licz na to.',
                'Nie.',
                'Moje źródła mówią że nie.',
                'Nie wygląda to zbyt dobrze',
                'Bardzo wątpliwe.']
        embed = discord.Embed(color=0x000033)
        embed.description = f'Pytanie: {question}\nOdpowiedź: {random.choice(responses)}'
        await ctx.send(embed=embed)


    @commands.command()
    async def wallpaper(self, ctx):
        embed = discord.Embed(color=0x000033)
        embed.set_image(url=nekos.img("wallpaper"))
        await ctx.send(embed=embed)


    @commands.command()
    async def neko(self, ctx):
        embed = discord.Embed(color=0x000033)
        embed.set_image(url=nekos.img("neko"))
        await ctx.send(embed=embed)
    
    #@commands.command()
    #async def bruh(self, ctx, msg):
        #embed = discord.Embed(color=0x000033)
        #embed.set_image(url=nekos.img(msg))
        #await ctx.send(embed=embed)
    
    @commands.command()
    async def waifu(self, ctx):
        response = requests.get("http://api.nekos.fun:8080/api/waifu")
        data = response.json()
        msg = f"Waifu :3"
        embed = discord.Embed(description=msg, color=0x000033)
        embed.set_image(url=data["image"])
        await ctx.send(embed=embed)


    @commands.command()
    async def cat(self, ctx):
        embed = discord.Embed(color=0x000033)
        embed.set_image(url=nekos.cat())
        await ctx.send(embed=embed)


    @commands.command()
    async def textcat(self, ctx):
        await ctx.send(nekos.textcat())


    @commands.command()
    async def pancake(self, ctx, member: discord.Member):
        embed=discord.Embed(title="🥞 Oddano naleśnika!", description=f"{ctx.author.mention} oddał naleśnika {member.mention}", color=0x000033)
        await ctx.send(embed=embed)


    @commands.command()
    async def pp(self, ctx, member: discord.Member):
        responses = ['8D',
                    '8=D',
                    '8==D',
                    '8===D',
                    '8====D',
                    '8=====D',
                    '8======D',
                    '8=======D',
                    '8========D',
                    '8=========D',
                    '8==========D',
                    '8===========D',
                    '8============D',
                    '8=============D']
        embed = discord.Embed(color=0x000033)
        embed.description = f'Dick {member.mention}: {random.choice(responses)}'
        await ctx.send(embed=embed)


    @commands.command()
    async def gaymeter(self, ctx, member: discord.Member):
        if member == None:
            member = ctx.author
        value = random.randint(0, 100)
        embed = discord.Embed(color=0x000033)
        embed.description = member.mention + " jest w " + str(value) + "% gejowy"
        await ctx.send(embed=embed)

    @commands.command()
    async def ship(self, ctx, member1: discord.Member, member2: discord.Member):
        value = random.randint(0, 100)
        embed = discord.Embed(color=0x000033)
        embed.description = member1.mention + " + "+ member2.mention +" = "+ str(value) + " %"
        await ctx.send(embed=embed)
    
    
def setup(bot):
    bot.add_cog(Fun(bot))