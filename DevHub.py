import discord 
from discord.ext import commands
import asyncio

bot = commands.Bot(command_prefix='dh')

@bot.event
async def on_ready():
    print('Bot is ready!')
    print(bot.user.name)
    print(bot.user.id)
    
bot.run('NjE4NTc5MDk5MjM3MjIwMzY2.XW7vUA.EPqoyGBrtPuqPEkKRdd9wMP8Ps8')
