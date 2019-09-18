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
    await bot.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name="n!help | n!info | n!invite"))
    print("Neon has started!")

@bot.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.send('Missing Required Arguments')

def owner(ctx):

    return ctx.author.id in (349499497774055429, 505366642230951984)

def boost(ctx):
    
    return ctx.message.author.id in (349499497774055429, 505366642230951984, 578978159488270358, 333972753659068416, 405266248314781696, 502562008420450305)
            
#--------------------------------------------------------------------------------------------------------------------------#
@bot.command()
@commands.check(boost)
async def ping(ctx):
    start = time.monotonic()
    embed = discord.Embed(title="Neon Premium's Ping!", color=0x0084FD)
    embed.add_field(name="Ping Latency", value="{} ms".format(int(ctx.bot.latency*1000)))
    await ctx.send(embed=embed)
@ping.error
async def ping_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("Premium Required Type n!info")
 
 
@bot.command()
async def help(ctx):
    embed=discord.Embed(title="Neon Premium Bot", url="https://discord.gg/WqtTxNV", color=0xbd00c7)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/618440592459956224/621380992988348421/national.jpg")
    embed.add_field(name="General" , value="General Commands", inline=True)
    embed.add_field(name="n!help", value="Shows This Message", inline=True)            
    embed.add_field(name="n!ping" , value="Displays Bot Latency", inline=True)
    embed.add_field(name="n!dm", value="Dm Mentioned User A Message", inline=True)
    embed.add_field(name="n!invite", value="Displays Bot Invite", inline=True)
    embed.add_field(name="n!avatar", value="Shows Mentioned Users Avatar", inline=True)   
    embed.add_field(name="n!serverinfo",value="Displays Server Stats", inline=True)
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

@bot.command()
@commands.check(boost)
async def dm(ctx, user: discord.Member, *, msg):
    dm = await user.create_dm()
    await dm.send(f"Sent By: {ctx.author.name}\nFrom Server: {ctx.guild.name}\nMessage: {msg}") 
    await ctx.send(f"Message Sent")
    await ctx.message.delete()
@dm.error
async def dm_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("Premium Required Type n!info")

@bot.command()
async def invite(ctx):
    embed = discord.Embed(title="Neon Premium - Invites", color=0x6AA84F)
    embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/618579099237220366/462cebed57fea3bad062f9982aa5fc02.png?")
    embed.add_field(name='**Invite Neon**', value="[Invite Neon](https://discordapp.com/oauth2/authorize?client_id=618579099237220366&scope=bot&permissions=2146958847)", inline=False)
    embed.add_field(name='**Support Server**', value="[Support](https://discord.gg/WqtTxNV)", inline=False)
    await ctx.send(embed=embed)
   
@bot.command()
@commands.check(boost)
async def avatar(ctx, member: discord.Member):
	embed = discord.Embed(colour=member.color, timestamp=ctx.message.created_at)
	embed.set_author(name=f"Avatar Of {member}")
	embed.set_image(url=member.avatar_url)
	await ctx.send(embed=embed)	
@avatar.error
async def avatar_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("Premium Required Type n!info")
        
@bot.command()  
@commands.check(boost)  
async def serverinfo(ctx):
    guild = ctx.message.guild
    online = len([m.status for m in guild.members if m.status == discord.Status.online or m.status == discord.Status.idle])
    embed = discord.Embed(name="{} Server information".format(guild.name), color=0x6AA84F)
    embed.set_thumbnail(url=guild.icon_url)
    embed.add_field(name="Server Name", value=guild.name, inline=True)
    embed.add_field(name="Owner", value=guild.owner.mention)
    embed.add_field(name="Server ID", value=guild.id, inline=True)
    embed.add_field(name="Roles", value=len(guild.roles), inline=True)
    embed.add_field(name="Members", value=len(guild.members), inline=True)
    embed.add_field(name="Online", value=f"**{online}/{len(guild.members)}**")
    embed.add_field(name="Guild Created At", value=guild.created_at.strftime("%d %b %Y %H:%M"))
    embed.add_field(name="Emojis", value=f"{len(guild.emojis)}/100")
    embed.add_field(name="Server Region", value=str(guild.region).title())
    embed.add_field(name="Total Channels", value=len(guild.channels))
    embed.add_field(name="AFK Channel", value=str(guild.afk_channel))
    embed.add_field(name="AFK Timeout", value=guild.afk_timeout)
    embed.add_field(name="Verification Level", value=guild.verification_level)
    await ctx.send(embed=embed)      
@serverinfo.error
async def serverinfo_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("Premium Required Type n!info")   
			   
bot.run(os.environ['TOKEN'])
