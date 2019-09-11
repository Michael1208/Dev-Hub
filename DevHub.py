import discord 
import os
from discord.ext import commands
import asyncio
import time

bot = commands.Bot(command_prefix='n!')
TOKEN = os.environ['TOKEN']

@bot.event
async def on_ready():
    print('Bot is ready!')
    print(bot.user.name)
    print(bot.user.id)
    
@bot.command()
async def ping(ctx):
    start = time.monotonic()
    embed = discord.Embed(title="Dragon's Ping!", color=0x0084FD)
    embed.add_field(name="latency", value="{} ms".format(int(ctx.bot.latency*1000)))
    await ctx.send(embed=embed)

@bot.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = ['It Is Certain',
    'Without A Doubt',
    'Yes Definitely',
    'You May Rely On It',
    'Most Likely',
    'Ask Again Later',
    'Nope',
    'Cannot Tell Right Now']
        
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

@bot.command()
async def rank(ctx):
    embed = discord.Embed(title="Rank!", color=0x0084FD)
    embed.add_field(name="Level", value=f"{user['lvl']}")
    embed.add_field(name="XP", value=f"{user['xp']}")
    await ctx.send(embed=embed)

@bot.command(pass_context=True, brief="DO THIS BEFORE ANYTHING ELSE! (ONLY ONCE)", aliases=['reg'])
async def register(ctx):
    id = str(ctx.message.author.id)
    if id not in amounts:
        amounts[id] = START_BALANCE
        await ctx.send(ctx.message.author.mention + ", You are now registered")
        print(id + " just made an account")
        print("have to take a dump")
        _save()
    else:
        await ctx.send(ctx.message.author.mention + ", You already have an account")
        print(id + " just tried to make an account, but already had one")

@bot.command(pass_context=True, brief="Shows your balance", aliases=['bal', 'b'])
    # @commands.cooldown(1, 30, commands.BucketType.user) this is the cooldown
    async def balance(ctx):
        id = str(ctx.message.author.id)
        if id in amounts:
            await ctx.send(ctx.message.author.mention + " has {} ".format(amounts[id]) + CURRENCY_NAME + " in the bank")
            print("Checked balance of " + id)
        else:
            await ctx.send("You do not have an account")
            print("Tried to check balance, but no account")



bot.run(TOKEN)
