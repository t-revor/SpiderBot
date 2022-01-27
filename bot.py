import discord
from discord.ext import commands
import random
import re

description = '''Discord bot in Python3 coded by Arachnomancer, aka t-revor for his discord of friends.
    For more information type !credit'''

TOKEN = '---token---'
intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', description=description, intents=intents)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.event
async def on_message(message):
    if bot.user.id != message.author.id:
        if 'hello' in message.content:
            await message.channel.send('Hello!')
    await bot.process_commands(message)

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return
    if rolls > 20:
        await ctx.send('Please roll less dices! Max is 20 rolls.')
        return
    elif limit >100:
        await ctx.send('Please choose a smaller dice! Max is d100.')
    else:
        result = [random.randint(1, limit) for r in range(rolls)]
        await ctx.send(f'You rolled {result}, for a total of: {sum(result)}.')

@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))

@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send('{0.name} joined in {0.joined_at}'.format(member))

@bot.command()
async def credit(ctx):
    """Posts the creator's GitHub page."""
    await cttx.send('```https://github.com/t-revor```')
 
bot.run(TOKEN)
