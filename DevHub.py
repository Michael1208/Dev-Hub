import discord 
import os
import asyncio
import time
from discord.ext import commands, tasks
from itertools import cycle

bot = commands.Bot(command_prefix='n!')
TOKEN = os.environ['TOKEN']
bot.remove_command('help')

@bot.event
async def on_ready():
        bot.status = cycle(['Neon Premium', 'n!help','Get Me By Boosting'])    
        change_status.start()                   
        print("Neon has started!")

@tasks.loop(seconds=15)
async def change_status():
  await bot.change_presence(activity=discord.Game(next(bot.status)))
    
@bot.command()
async def ping(ctx):
    start = time.monotonic()
    embed = discord.Embed(title="Neon Premium's Ping!", color=0x0084FD)
    embed.add_field(name="latency", value="{} ms".format(int(ctx.bot.latency*1000)))
    await ctx.send(embed=embed)
 
@bot.command()
async def help(ctx):
    embed=discord.Embed(title="Neon Premium", url="https://discord.gg/WqtTxNV", color=0xbd00c7)
    embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/616619124730363924/6721a098ceee307c2a32ba8de4332ff0.png?")
    embed.add_field(name="Music" , value="Music Commands", inline=True)
    embed.add_field(name="Commands Here", value="Command", inline=True)
    embed.add_field(name="Economy", value="Economy Commands" , inline=True)
    embed.add_field(name="Commands Here", value="Command", inline=True)
    embed.set_footer(text="Neon™ Premium Bot")
    await ctx.send(embed=embed)
