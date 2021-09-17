import discord
from discord.ext import commands
import os


intents = discord.Intents.default()
intents.members = True
intents.presences = True
bot = commands.Bot(command_prefix= ">",intents=intents)
version = 1
bot.remove_command('help')



# Events
@bot.event
async def on_ready():
    await bot.change_presence(
        activity=discord.Game(name="use >help to see what i do"))
    print('Main file loaded.Good to go!')


@bot.listen()
async def on_message(message):
    if "hello dum bot" in message.content.lower():
        # in this case don't respond with the word "Tutorial" or you will call the on_message event recursively
        await message.channel.send('Hello')
        await bot.process_commands(message)


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

# EXECUTES THE BOT WITH THE SPECIFIED TOKEN. TOKEN HAS BEEN REMOVED AND USED JUST AS AN EXAMPLE.
bot.run("ODA3OTI2MjA5MDQ0MjgzNDIy.YB_F6g.R27semiXbFO2qztWBxEQqmFXPi0")
