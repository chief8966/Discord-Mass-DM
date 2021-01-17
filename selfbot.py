import discord
import asyncio
from discord.ext import commands

token = 'Nzg4MDYxNzkwOTEwOTM5MTM5.X9eBvA.bADf1nEY8L-ukShn9wdEdPoe-ps'

prefix = 'gay!'
client = discord.Client()
client = commands.Bot(
    description='Dropout',
    command_prefix=prefix,
    self_bot=True
)
client.remove_command('help') 

@client.event
async def on_ready():
    print('Online')
   

@client.command()
async def dmall(ctx, *, message):
    for user in list(ctx.guild.members):
        try:
            await user.send(message)
            print(f"Sent To {user}")
        except:
            pass

    
client.run(token, bot = False)
