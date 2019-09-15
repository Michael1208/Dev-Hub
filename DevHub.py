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

def owner(ctx):

    return ctx.author.id in (349499497774055429, 505366642230951984)

     

class CantDoThatCommand(commands.CommandError):
    pass

@bot.check
def boost(ctx):
    if ctx.message.author.id not in (349499497774055429, 505366642230951984, 578978159488270358):
        raise CantDoThatCommand("Premium Required Type n!info")
    return True

@bot.event
async def on_command_error(ctx, error):
    if type(error).__name__ == "CantDoThatCommand":
        await ctx.send("Premium Required Type n!info For More Information")
            
        
@bot.command()
@commands.check(boost)
async def ping(ctx):
    start = time.monotonic()
    embed = discord.Embed(title="Neon Premium's Ping!", color=0x0084FD)
    embed.add_field(name="Ping Latency", value="{} ms".format(int(ctx.bot.latency*1000)))
    await ctx.send(embed=embed)
 
@bot.command()
async def help(ctx):
    embed=discord.Embed(title="Neon Premium Bot", url="https://discord.gg/WqtTxNV", color=0xbd00c7)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/618440592459956224/621380992988348421/national.jpg")
    embed.add_field(name="General" , value="General Commands", inline=True)
    embed.add_field(name="n!ping" , value="Displays Bot Latency", inline=True)
    embed.set_footer(text="Neon™ Premium Bot")
    await ctx.send(embed=embed)
 
@bot.command()
async def info(ctx):
    embed=discord.Embed(title="Click To Join Support Server", url="https://discord.gg/WqtTxNV", color=0xbd00c7)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/618440592459956224/621380992988348421/national.jpg")
    embed.add_field(name="How To Get Neon Premium" , value="Neon Premium Can Be Recieved By Boosting The Support Server Link Above Premium Will Offer Commands That The Normal Bot Doesn't Such As Economy And Music", inline=True)
    embed.set_footer(text="Neon™ Premium Bot")
    await ctx.send(embed=embed)

@bot.command()
@commands.check(owner)
async def servers(ctx):
    string = "\n".join([f"Server: {g.name} Users: {len(g.members)}" for g in bot.guilds])
    await ctx.send(f"I'm Currently In These Severs- \n {string}")
@servers.error
async def servers_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("Error Bot Developers Only")   
 
@bot.command(pass_context=True)

async def virus(ctx, hack=None):

    if not hack:

        hack = 'discord'

    else:

        hack = hack.replace(' ','_')

    channel = ctx.message.channel

    x = await ctx.send_message(channel, '``[▓▓▓                    ] / {}-virus.exe Packing files.``'.format(hack))

    await asyncio.sleep(1.5)

    x = await ctx.edit_message(x,'``[▓▓▓▓▓▓▓                ] - {}-virus.exe Packing files..``'.format(hack))

    await asyncio.sleep(0.3)

    x = await ctx.edit_message(x,'``[▓▓▓▓▓▓▓▓▓▓▓▓           ] \ {}-virus.exe Packing files...``'.format(hack))

    await asyncio.sleep(1.2)

    x = await ctx.edit_message(x,'``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓         ] | {}-virus.exe Initializing code.``'.format(hack))

    await asyncio.sleep(1)

    x = await ctx.edit_message(x,'``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓      ] / {}-virus.exe Initializing code..``'.format(hack))

    await asyncio.sleep(1.5)

    x = await ctx.edit_message(x,'``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓   ] - {}-virus.exe Finishing.``'.format(hack))

    await asyncio.sleep(1)

    x = await ctx.edit_message(x,'``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ] \ {}-virus.exe Finishing..``'.format(hack))

    await asyncio.sleep(1)

    x = await ctx.edit_message(x,'``Successfully downloaded {}-virus.exe``'.format(hack))

    await asyncio.sleep(2)

    x = await ctx.edit_message(x,'``Injecting virus.   |``')

    await asyncio.sleep(0.5)

    x = await ctx.edit_message(x,'``Injecting virus..  /``')

    await asyncio.sleep(0.5)

    x = await ctx.edit_message(x,'``Injecting virus... -``')

    await asyncio.sleep(0.5)

    x = await ctx.edit_message(x,'``Injecting virus....\``')

    await ctx.delete_message(x)

    await ctx.delete
        

bot.run(os.environ['TOKEN'])
