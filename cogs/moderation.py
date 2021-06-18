import discord
from discord.ext import commands
import asyncio
from datetime import datetime

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    #Events
    @commands.Cog.listener()
    async def on_ready(self):
        print("Cog Moderation is ready")
    
    
    @commands.command()
    @commands.has_permissions(kick_members = True)
    async def mute(self, ctx, user : discord.Member, time: int, *, powod = None):
        if ctx.author == user:
            await ctx.send("Nie możesz zmutować sam siebie!")
            return 0
        muted = ctx.guild.get_role(772478549797371950)
        embed = discord.Embed(color = 0x000033)
        if powod is not None: 
            embed.description = user.mention + " został zmutowany z powodu: " + powod + "'"
        else:
            embed.description = user.mention + " został zmutowany"
        await user.add_roles(muted)
        await ctx.send(embed=embed)
        if time != 0:
            time = time * 60
            await asyncio.sleep(time)
            await user.remove_roles(muted)
    
    @commands.command()
    @commands.has_permissions(kick_members = True)
    async def unmute(self, ctx, user : discord.Member, *, powod = None):
        embed = discord.Embed(color=0x000033)
        muted = ctx.guild.get_role(772478549797371950)
        if powod is not None:
            embed.description = user.mention + " został odmutowany z powodu: '" + powod +"'"
        else:
            embed.description = user.mention + " został odmutowany"
        await user.remove_roles(muted)
        await ctx.send(embed=embed)
    
    @commands.command()
    @commands.has_permissions(kick_members = True)
    async def warn(self, ctx, user : discord.Member, *, powod = None):
        embed = discord.Embed(color=0x000033)
        if powod is not None:
            embed.description = user.mention + " został ostrzeżony z powodu: " + powod + "'"
        else:
            embed.description = user.mention + " został ostrzeżony"
        await ctx.send(embed=embed)
    
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=5):
        await ctx.channel.purge(limit=amount+1)
    
    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        if ctx.author == member:
            await ctx.send("Nie możesz zbanować sam siebie!")
            return 0
        await member.ban(reason=reason) 
        if reason == None:
            reason = "n/a"
        now = datetime.now()
        member = member.mention
        embed=discord.Embed(title=f"{member.name} został zbanowany", color=0x000033)
        embed.add_field(name="**Moderator odpowiedzialny za bana:**", value=f"{ctx.author.mention}", inline=False)
        embed.add_field(name="**Powód bana:**", value=f"{reason}", inline=False)
        embed.add_field(name="**Czas**", value=now, inline=False)
        embed.set_image(url="https://media1.tenor.com/images/8271ab57eccd9de0850d0e277e2eabd0/tenor.gif?itemid=19920592")
        await ctx.send(embed=embed)
    
    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split("#")
    
        for ban_entry in banned_users:
            user = ban_entry.user
    
            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Odbanowano {user.mention}')
                return
    
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        if ctx.author == member:
            await ctx.send("Nie możesz wyrzucić sam siebie!")
            return 0
        if reason == None:
            reason = "n/a"
        embed=discord.Embed(title=f"{member.name} został wyrzucony", color=0x000033)
        embed.add_field(name="**Moderator odpowiedzialny za kick:**", value=f"{ctx.author.mention}", inline=False)
        embed.add_field(name="**Powód kicka:**", value=f"{reason}", inline=False)
        embed.add_field(name="**Czas**", value="n/a", inline=False)
        embed.set_image(url="https://media1.tenor.com/images/fb2a19c9b689123e6254ad9ac6719e96/tenor.gif?itemid=4922649")
        await ctx.send(embed=embed)

        await member.kick(reason=reason)
    
def setup(bot):
    bot.add_cog(Moderation(bot))