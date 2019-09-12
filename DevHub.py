import discord 
import os
import asyncio
import time
from discord.ext import commands, tasks
from itertools import cycle

bot = commands.Bot(command_prefix='n!')
bot.remove_command('help')

@bot.event
async def on_ready():        
    await bot.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name="n!help | n!info"))
    print("Neon has started!")
    
@bot.command()
async def ping(ctx):
    start = time.monotonic()
    embed = discord.Embed(title="Neon Premium's Ping!", color=0x0084FD)
    embed.add_field(name="latency", value="{} ms".format(int(ctx.bot.latency*1000)))
    await ctx.send(embed=embed)
 
@bot.command()
async def help(ctx):
    embed=discord.Embed(title="Neon Premium", url="https://discord.gg/WqtTxNV", color=0xbd00c7)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/618440592459956224/621380992988348421/national.jpg")
    embed.add_field(name="Music" , value="Music Commands", inline=True)
    embed.add_field(name="Commands Here", value="Command", inline=True)
    embed.add_field(name="Economy", value="Economy Commands" , inline=True)
    embed.add_field(name="Commands Here", value="Command", inline=True)
    embed.set_footer(text="Neon™ Premium Bot")
    await ctx.send(embed=embed)
 
@bot.command()
async def info(ctx):
    embed=discord.Embed(title="How To Get Neon Premium", url="https://discord.gg/WqtTxNV", color=0xbd00c7)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/618440592459956224/621380992988348421/national.jpg")
    embed.add_field(name="How To Get Neon Premium" , value="Neon Premium Can Be Recieved By Boosting The Support Server Link Above Premium Will Offer Commands That The Normal Bot Doesn't Such As Economy And Music", inline=True)
    embed.set_footer(text="Neon™ Premium Bot")
    await ctx.send(embed=embed)

@bot.command()
async def say(ctx, content):
    if content == ["@everyone"]:
        await ctx.send("You cannot mention **@**everyone, silly. I don't want to get banned.")
        pass
    elif content == ["@here"]:
        await ctx.send("You cannot mention **@**here, silly. I don't want to get banned.")
        pass
    else:
        await ctx.send(content)
        await ctx.message.delete()

bot.run(os.environ['TOKEN'])
