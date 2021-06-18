import discord
from discord.ext import commands

from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
from datetime import datetime

class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    
    intents = discord.Intents.all()
    client = discord.Client(intents=intents)
    

    #Events
    @commands.Cog.listener()
    async def on_ready(self):
        print("Cog Utility is ready")


    @commands.Cog.listener()
    async def on_member_join(self, member):
        embed = discord.Embed(title=f"{member.name} witaj na serwerze {member.guild.name}!", description="Zapraszamy do przeczytania regulaminu i przyznania sobie ról! Miłej zabawy!!", inline=False, color = 0x000033)
        true_member_count = len([m for m in member.guild.members if not m.bot])
        now = datetime.now()
        embed.timestamp= datetime.now()
        embed.set_footer(text=f"Jest nas {true_member_count}")
        embed.set_image(url="https://cdn.discordapp.com/attachments/716750707252002917/802966344064696351/c996e3ff8746f9a904f39604e24a4021.gif")
        #embed.set_thumbnail(url="https://i.pinimg.com/originals/6a/86/22/6a86228d9b059d153f90a2884ecb0c40.gif")
        channel = discord.utils.get(member.guild.channels, id=int("806881854790828042"))
        await channel.send(embed = embed)


    @commands.Cog.listener()
    async def on_member_remove(self, member):
        embed = discord.Embed(title=f"{member.name} opuścił serwer {member.guild.name}", inline=False, color = 0x000033)
        true_member_count = len([m for m in member.guild.members if not m.bot])
        now = datetime.now()
        embed.timestamp= datetime.now()
        embed.set_footer(text=f"Jest nas {true_member_count}")
        embed.set_image(url="https://cdn.discordapp.com/attachments/734685903712419881/812361500567142521/1e934804a7d3f6db63a3a04d27ce808f.gif")
        #embed.set_thumbnail(url="https://i.pinimg.com/originals/6a/86/22/6a86228d9b059d153f90a2884ecb0c40.gif")
        channel = discord.utils.get(member.guild.channels, id=int("806881854790828042"))
        await channel.send(embed = embed)


    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        message_id = payload.message_id
        if message_id == 772483661257637900:
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g: g.id == guild_id, self.bot.guilds)

            if payload.emoji.name == "SataniaThumbsUp":
                role = discord.utils.get(guild.roles, name="Słodziak")
            else:
                role = discord.utils.get(guild.roles, name=payload.emoji.name)
            if role is not None:
                member = payload.member
                if member is not None:
                    await member.add_roles(role)
                    print(f"Added {member} role {role}")
                else:
                    print("Member not found")
            else:
                print("Role not found")
        elif message_id == 784793081781289021:
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g: g.id == guild_id, self.bot.guilds)

            if payload.emoji.name == "💚":
                role = discord.utils.get(guild.roles, name="Zielony")
            elif payload.emoji.name == "💛":
                role = discord.utils.get(guild.roles, name="Żółty")
            elif payload.emoji.name == "💙":
                role = discord.utils.get(guild.roles, name="Niebieski")
            elif payload.emoji.name == "💗":
                role = discord.utils.get(guild.roles, name="Fioletowy")
            elif payload.emoji.name == "🤍":
                role = discord.utils.get(guild.roles, name="Bialy")
            elif payload.emoji.name == "💖":
                role = discord.utils.get(guild.roles, name="Złoty")
            elif payload.emoji.name == "💟":
                role = discord.utils.get(guild.roles, name="Srebrny")
            elif payload.emoji.name == "💓":
                role = discord.utils.get(guild.roles, name="Zieleń")
            elif payload.emoji.name == "🧡":
                role = discord.utils.get(guild.roles, name="Pomarańczowy")
            elif payload.emoji.name == "❤️":
                role = discord.utils.get(guild.roles, name="Czerwony")
            elif payload.emoji.name == "❣️":
                role = discord.utils.get(guild.roles, name="Różowy")
            elif payload.emoji.name == "🖤":
                role = discord.utils.get(guild.roles, name="Czarny")
            else:
                role = discord.utils.get(guild.roles, name=payload.emoji.name)
            if role is not None:
                member = discord.utils.get(guild.members, id=payload.user_id)
                if member is not None:
                    await member.add_roles(role)
                    print(f"Added {member} role {role}")
                else:
                    print("Member not found")
            else:
                print("Role not found")
        elif message_id == 784793094406144000:
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g: g.id == guild_id, self.bot.guilds)

            if payload.emoji.name == "💻":
                role = discord.utils.get(guild.roles, name="Programowanie")
            elif payload.emoji.name == "🍜":
                role = discord.utils.get(guild.roles, name="Manga")
            elif payload.emoji.name == "🇯🇵":
                role = discord.utils.get(guild.roles, name="Anime")
            elif payload.emoji.name == "📺":
                role = discord.utils.get(guild.roles, name="Seriale")
            elif payload.emoji.name == "Kitsu":
                role = discord.utils.get(guild.roles, name="Pisanie")
            elif payload.emoji.name == "FroggBlush":
                role = discord.utils.get(guild.roles, name="Rysowanie")
            else:
                role = discord.utils.get(guild.roles, name=payload.emoji.name)
            if role is not None:
                member = payload.member
                if member is not None:
                    await member.add_roles(role)
                    print(f"Added {member} role {role}")
                else:
                    print("Member not found")
            else:
                print("Role not found")
        elif message_id == 784793109233926205:
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g: g.id == guild_id, self.bot.guilds)

            if payload.emoji.name == "Awoo":
                role = discord.utils.get(guild.roles, name="Chłopak")
            elif payload.emoji.name == "Awooo":
                role = discord.utils.get(guild.roles, name="Dziewczyna")
            elif payload.emoji.name == "PikaPickaxe":
                role = discord.utils.get(guild.roles, name="Minecraft")
            elif payload.emoji.name == "akali_kda_huh":
                role = discord.utils.get(guild.roles, name="League of Legends")
            elif payload.emoji.name == "AmongUsRed":
                role = discord.utils.get(guild.roles, name="Among Us")
            elif payload.emoji.name == "nohomo":
                role = discord.utils.get(guild.roles, name="Ankiety")
            else:
                role = discord.utils.get(guild.roles, name=payload.emoji.name)
            if role is not None:
                member = payload.member
                if member is not None:
                    await member.add_roles(role)
                    print(f"Added {member} role {role}")
                else:
                    print("Member not found")
            else:
                print("Role not found")


    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        message_id = payload.message_id
        if message_id == 772483661257637900:
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g: g.id == guild_id, self.bot.guilds)

            if payload.emoji.name == "SataniaThumbsUp":
                role = discord.utils.get(guild.roles, name="Słodziak")
            else:
                role = discord.utils.get(guild.roles, name=payload.emoji.name)
            if role is not None:
                member = discord.utils.get(guild.members, id=payload.user_id)
                print(member)
                if member is not None:
                    await member.remove_roles(role)
                    print(f"Removed {member} role {role}")
                else:
                    print("Member not found")
            else:
                print("Role not found")
        elif message_id == 784793081781289021:
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g: g.id == guild_id, self.bot.guilds)

            if payload.emoji.name == "💚":
                role = discord.utils.get(guild.roles, name="Zielony")
            elif payload.emoji.name == "💛":
                role = discord.utils.get(guild.roles, name="Żółty")
            elif payload.emoji.name == "💙":
                role = discord.utils.get(guild.roles, name="Niebieski")
            elif payload.emoji.name == "💗":
                role = discord.utils.get(guild.roles, name="Fioletowy")
            elif payload.emoji.name == "🤍":
                role = discord.utils.get(guild.roles, name="Bialy")
            elif payload.emoji.name == "💖":
                role = discord.utils.get(guild.roles, name="Złoty")
            elif payload.emoji.name == "💟":
                role = discord.utils.get(guild.roles, name="Srebrny")
            elif payload.emoji.name == "💓":
                role = discord.utils.get(guild.roles, name="Zieleń")
            elif payload.emoji.name == "🧡":
                role = discord.utils.get(guild.roles, name="Pomarańczowy")
            elif payload.emoji.name == "❤️":
                role = discord.utils.get(guild.roles, name="Czerwony")
            elif payload.emoji.name == "❣️":
                role = discord.utils.get(guild.roles, name="Różowy")
            elif payload.emoji.name == "🖤":
                role = discord.utils.get(guild.roles, name="Czarny")
            else:
                role = discord.utils.get(guild.roles, name=payload.emoji.name)
            if role is not None:
                member = discord.utils.get(guild.members, id=payload.user_id)
                print(member)
                if member is not None:
                    await member.remove_roles(role)
                    print(f"Removed {member} role {role}")
                else:
                    print("Member not found")
            else:
                print("Role not found")
        elif message_id == 784793094406144000:
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g: g.id == guild_id, self.bot.guilds)

            if payload.emoji.name == "💻":
                role = discord.utils.get(guild.roles, name="Programowanie")
            elif payload.emoji.name == "🍜":
                role = discord.utils.get(guild.roles, name="Manga")
            elif payload.emoji.name == "🇯🇵":
                role = discord.utils.get(guild.roles, name="Anime")
            elif payload.emoji.name == "📺":
                role = discord.utils.get(guild.roles, name="Seriale")
            elif payload.emoji.name == "Kitsu":
                role = discord.utils.get(guild.roles, name="Pisanie")
            elif payload.emoji.name == "FroggBlush":
                role = discord.utils.get(guild.roles, name="Rysowanie")
            elif payload.emoji.name == "nohomo":
                role = discord.utils.get(guild.roles, name="Ankiety")
            else:
                role = discord.utils.get(guild.roles, name=payload.emoji.name)
            if role is not None:
                member = discord.utils.get(guild.members, id=payload.user_id)
                print(member)
                if member is not None:
                    await member.remove_roles(role)
                    print(f"Removed {member} role {role}")
                else:
                    print("Member not found")
            else:
                print("Role not found")
        elif message_id == 784793109233926205:
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g: g.id == guild_id, self.bot.guilds)

            if payload.emoji.name == "Awoo":
                role = discord.utils.get(guild.roles, name="Chłopak")
            elif payload.emoji.name == "Awooo":
                role = discord.utils.get(guild.roles, name="Dziewczyna")
            elif payload.emoji.name == "PikaPickaxe":
                role = discord.utils.get(guild.roles, name="Minecraft")
            elif payload.emoji.name == "akali_kda_huh":
                role = discord.utils.get(guild.roles, name="League of Legends")
            elif payload.emoji.name == "AmongUsRed":
                role = discord.utils.get(guild.roles, name="Among Us")
            elif payload.emoji.name == "nohomo":
                role = discord.utils.get(guild.roles, name="Ankiety")
            else:
                role = discord.utils.get(guild.roles, name=payload.emoji.name)
            if role is not None:
                member = discord.utils.get(guild.members, id=payload.user_id)
                print(member)
                if member is not None:
                    await member.remove_roles(role)
                    print(f"Removed {member} role {role}")
                else:
                    print("Member not found")
            else:
                print("Role not found")


    @commands.command()
    @commands.has_role('Ankiety')
    async def poll(self, ctx, *,question):
        embed = discord.Embed(description="TAK ✅ \n NIE ❌",title=question, color=0x000033)
        embed.timestamp= datetime.now()
        now = datetime.now()
        await ctx.channel.purge(limit=1)
        react = await ctx.send(embed=embed)
        await react.add_reaction('✅')
        await react.add_reaction('❌') 
    
    @commands.command()
    async def serverinfo(self, ctx):
        server = ctx.message.guild
        roles = [x.name for x in server.roles]
        role_length = len(roles)
        if role_length > 50:
            roles = roles[:50]
            roles.append('>>>> Wyświetlam[50/%s] Rang' % len(roles))
        roles = ', '.join(roles)
        channels = len(server.channels)
        time = str(server.created_at)
        time = time.split(' ')
        time = time[0]
        embed = discord.Embed(description='%s    ' % (str(server)), title='**Nazwa Serwera:**', color=0x000033)
        embed.set_thumbnail(url=server.icon_url)
        embed.add_field(name='__Wlaściciel__', value=str(server.owner) + '\n')
        embed.add_field(name='__Server ID__', value=str(server.id))
        embed.add_field(name='__Licznik Członków__', value=str(server.member_count))
        embed.add_field(name='__Kanały Tekstowe/Głosowe__', value=str(channels))
        embed.add_field(name='__Role (%s)__' % str(role_length), value=roles)
        embed.set_footer(text='Stworzony: %s' % time)
        await ctx.message.channel.send(embed=embed)


    @commands.command()
    async def avatar(self, ctx, member: discord.Member = None):
        if member == None:
            member = ctx.author
        if member is None:
            member = ctx.message.author
        await ctx.send(member.avatar_url)


    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Pong! Opóźnienie: {round(self.bot.latency * 1000)}ms')


    @commands.command()
    async def help(self, ctx):
        embed=discord.Embed(title="Lista dostępnych komend(prefix $)", color=0x000033)
        embed.add_field(name="Komendy Emotes", value="`smug` `thumbsup` `baka` `facepalm` `confused` `facedesk` `angry` `drink` `cry` `cool` `grin` `happy` `think` `dance` `sleepy` `blush` `pout` `shrug` `initiald`", inline=False)
        embed.add_field(name="Komendy Economy", value="`balance` `withdraw` `deposit` `send` `slots` `beg` `rob`", inline=False)
        embed.add_field(name="Komendy Action", value="`pat` `hug` `kiss` `feed` `tickle` `poke` `kill` `marry` `choke` `slap`  `cuddle` `wave` `bite` `highfive` `handhold`", inline=False)
        embed.add_field(name="Komendy Fun", value="`gay` `triggered` `wasted` `waifumeter` `8ball` `wallpaper` `neko` `waifu` `cat` `textcat` `pp` `gaymeter`", inline=False)
        embed.add_field(name="Komendy Util", value="`serverinfo` `avatar` `help`", inline=False)
        embed.add_field(name="Komendy Moderation", value="`clear` `ban` `unban` `mute` `unmute` `kick`", inline=False)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Utility(bot))
