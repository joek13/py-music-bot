import discord, config, logging
from discord.ext import commands

CONFIG = config.load_config() # load the config file

bot = commands.Bot(command_prefix="^")

@bot.event
async def on_ready():
    logging.info(f"Logged in as {bot.user.name}")

def run():
    bot.run(CONFIG["token"])
