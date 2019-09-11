import discord 
import os
from discord.ext import commands
import asyncio
import time

bot = commands.Bot(command_prefix='>')
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

@bot.command(pass_context=True, aliases=['j', 'joi'])
async def join(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()

    await voice.disconnect()

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
        print(f"The bot has connected to {channel}\n")

    await ctx.send(f"Joined {channel])

bot.run(TOKEN)
