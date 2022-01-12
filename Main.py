import discord
from discord.ext import commands
import Music

cogs= [music]

client = commands.Bot(command_prefix='?', intents = discord, intents = discord.Intents.all())

for i in range(len(cogs)):
    cogs[i].setup()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.author == client.user:
        return
    
    if message.channel.name == 'pp':
        if user_message.lower() == 'halo':
            await message.channel.send(f'halo {username}!')
            return
        elif user_message.lower() == 'ganteng':
            await message.channel.send(f'Si {username} memang ganteng')
            return

client.run(OTMwNjQ1Njc5ODI1NjQ1NTk4.Yd45VA.ZhslKq8s17MCm1oULzS9X3tWk08)