import discord, config, logging
from discord.ext import commands
from cogs import music, error

CONFIG = config.load_config() # load the config file

bot = commands.Bot(command_prefix="^")

@bot.event
async def on_ready():
    logging.info(f"Logged in as {bot.user.name}")

COGS = [
    music.Music,
    error.CommandErrorHandler
]

def add_cogs(bot):
    for cog in COGS:
        bot.add_cog(cog(bot)) # Initialize the cog and add it to the bot

def run():
    add_cogs(bot)
    bot.run(CONFIG["token"])
