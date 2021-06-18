import discord
from discord.ext import commands
import json
import os

import random

mainshop = [
    {"nazwa":"???","cena":"999999999", "opis":"What is it?"}
]

class Economy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    

    intents = discord.Intents.all()
    client = discord.Client(intents=intents)


    @commands.Cog.listener()
    async def on_ready(self):
        print("Cog Economy is ready")

    
    @commands.command()
    async def balance(self, ctx, member: discord.Member = None):
        await self.open_account(ctx.author)
        if member == None:
            user = ctx.author
        else:
            user = member
        users = await self.get_bank_data()

        wallet_amount = users[str(user.id)]['wallet']
        bank_amount = users[str(user.id)]['bank']

        embed = discord.Embed(title = f"Saldo {ctx.author.name}", color = 0x000033)
        embed.add_field(name = "Portfel ", value = wallet_amount)
        embed.add_field(name = "Bank ", value = bank_amount)
        await ctx.send(embed = embed)


    @commands.command()
    async def withdraw(self, ctx, amount = None):
        await self.open_account(ctx.author)
        if amount == None:
            await ctx.send("Nie możesz wypłacić niczego!")
            return
        balance = await self.update_bank(ctx.author)
        if amount == "all":
            user = ctx.author
            users = await self.get_bank_data()

            wallet_amount = users[str(user.id)]['wallet']
            await self.update_bank(ctx.author, wallet_amount)
            await self.update_bank(ctx.author, -1*wallet_amount, "bank")
            await ctx.send("Wypłaciłeś wszystko z banku!")
        amount = int(amount)
        if amount>balance[0]:
            await ctx.send("Nie masz tyle pieniędzy!")
            return
        if amount<0:
            await ctx.send("Musisz podać dodatnią liczbę")
       
        else:
            await self.update_bank(ctx.author, amount)
            await self.update_bank(ctx.author, -1*amount, "bank")
            await ctx.send(f"Wpłaciłeś {amount}🪙")




    @commands.command()
    async def shop(self, ctx):
        embed = discord.Embed(title = "Shop")
        for item in mainshop:
            name =  item["nazwa"]
            price =  item["cena"]
            desc =  item["opis"]
            embed.add_field(name = name, value = f"${price} | {desc}")
        
        await ctx.send(embed = embed)


    @commands.command()
    async def deposit(self, ctx, amount = None):
        await self.open_account(ctx.author)
        if amount == None:
            await ctx.send("Nie możesz wpłacić niczego!")
            return
        balance = await self.update_bank(ctx.author)
        if amount == "all":
            user = ctx.author
            users = await self.get_bank_data()

            wallet_amount = users[str(user.id)]['wallet']
            await self.update_bank(ctx.author, -1*wallet_amount)
            await self.update_bank(ctx.author, wallet_amount, "bank")
            await ctx.send("Wpłaciłeś wszystko do banku!")
        amount = int(amount)
        if amount>balance[0]:
            await ctx.send("Nie masz tyle pieniędzy!")
            return
        if amount<0:
            await ctx.send("Musisz podać dodatnią liczbę")
       
        else:
            await self.update_bank(ctx.author, -1*amount)
            await self.update_bank(ctx.author, amount, "bank")
            await ctx.send(f"Wpłaciłeś {amount}🪙")


    @commands.command()
    @commands.is_owner()
    async def clearbank(self, ctx, member: discord.Member):
        await self.open_account(ctx.author)
        user = ctx.author
        await self.dump_bank(user)
        
        await ctx.send("Zaki wyczyścił twój bank i portfel")


    @commands.command()
    async def send(self, ctx, member: discord.Member, amount = None):
        await self.open_account(ctx.author)
        await self.open_account(member)
        if amount == None:
            await ctx.send("Nie możesz wypłacić niczego!")
            return
        balance = await self.update_bank(ctx.author)
        amount = int(amount)
        if amount>balance[1]:
            await ctx.send("Nie masz tyle pieniędzy!")
            return
        if amount<0:
            await ctx.send("Musisz podać dodatnią liczbę")
            return
        await self.update_bank(ctx.author, -1*amount, "bank")
        await self.update_bank(member, amount, "bank")
        await ctx.send(f"Oddałeś {member.mention} {amount}🪙")

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command()
    async def slots(self, ctx, amount = None):
        await self.open_account(ctx.author)
        if amount == None:
            await ctx.send("Nie możesz wypłacić niczego!")
            return
        balance = await self.update_bank(ctx.author)
        amount = int(amount)
        if amount>balance[0]:
            await ctx.send("Nie masz tyle pieniędzy!")
            return
        if amount<0:
            await ctx.send("Musisz podać dodatnią liczbę")
            return

        final = []
        for i in range(3):
            a = random.choice(["🍇", "🍊", "🍌"])
            final.append(a)
        
        await ctx.send(str(final))
        if final[0] == final[1] or final[0] == final [2] or final[0] == final[3]:
            await self.update_bank(ctx.author, 2*amount)
            await ctx.send("Wygrałeś!")
        else:
            await self.update_bank(ctx.author, -1*amount)
            await ctx.send("Przegrałeś...")


    @commands.cooldown(1, 300, commands.BucketType.user)
    @commands.command()
    async def rob(self, ctx, member: discord.Member):
        await self.open_account(ctx.author)
        await self.open_account(member)
        balance = await self.update_bank(member)
        if balance[0]<100:
            await ctx.send("Ta osoba jest zbyt biedna by ją okraść")
            return
        
        earnings = random.randrange(0, balance[0])

        await self.update_bank(ctx.author, earnings)
        await self.update_bank(member, -1*earnings)
        await ctx.send(f"Okradłeś {member.mention} z {earnings}🪙")


    @commands.cooldown(1, 60, commands.BucketType.user)
    @commands.command()
    async def beg(self, ctx):
        await self.open_account(ctx.author)
        user = ctx.author
        users = await self.get_bank_data()

        earnings = random.randrange(101)
        await ctx.send(f"Ktoś dał ci {earnings}🪙")
        users[str(user.id)]['wallet'] += earnings
        with open('cogs/bank.json','w') as f:
            json.dump(users, f)

    #Error handling

    @commands.Cog.listener()
    async def on_command_error(self, message, error):
        if isinstance(error, commands.CommandOnCooldown):
            await message.channel.send(f'Ta komenda nie może jeszcze zostać użyta spróbuj za %.0f sekundy' % error.retry_after)

    async def open_account(self, user):  
        users = await self.get_bank_data()

        if str(user.id) in users:
            return False

        else:
            users[str(user.id)] = {}
            users[str(user.id)]['wallet'] = 0
            users[str(user.id)]['bank'] = 0

        with open('cogs/bank.json','w') as f:
            json.dump(users, f)
        return True


    async def get_bank_data(self):
        with open("cogs/bank.json", "r") as f:
            users = json.load(f)
        return users
    

    async def dump_bank(self, user):
        users = await self.get_bank_data()

        users[str(user.id)]['wallet'] = 0
        users[str(user.id)]['bank'] = 0



    async def update_bank(self, user, change=0, mode = "wallet"):
        users = await self.get_bank_data()

        users[str(user.id)][mode] += change 
        with open('cogs/bank.json','w') as f:
            json.dump(users, f)
        balance = [users[str(user.id)]["wallet"], users[str(user.id)]["bank"]]
        return balance


def setup(bot):
    bot.add_cog(Economy(bot))
