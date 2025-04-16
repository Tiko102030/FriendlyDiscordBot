import discord
from discord.ext import commands
from config import TOKEN
import time
import asyncio  # Add this import

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    try:
        synced = await bot.tree.sync()
        print(f'Synced {len(synced)} commands')
    except Exception as e:
        print(f'Error syncing commands: {e}')
        
@bot.tree.command(name='hello')
async def hello(interaction: discord.Interaction):
    # Send the first message using interaction.response
    await interaction.response.send_message(f'Hello {interaction.user.mention}!')
    
    # Use followup.send for subsequent messages
    for _ in range(20):  # 9 more messages to make a total of 10
        await interaction.followup.send(f'AHAHAHAHAH {_}')
        await asyncio.sleep(.1)  # Asynchronous sleep for .1 second


# @bot.command()
# async def hello(ctx):
#     await ctx.send('Hello!')

bot.run(TOKEN) # insert your token here