import discord
from discord.ext import commands
import Music

cogs= [music]

client = commands.Bot(command_prefix='?', intents = discord, intents = discord.Intents.all())

for i in range(len(cogs)):
    cogs[i].setup()


client.run(OTMwNjQ1Njc5ODI1NjQ1NTk4.Yd45VA.ZhslKq8s17MCm1oULzS9X3tWk08)