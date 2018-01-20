import discord, config, logging
from discord.ext import commands
from cogs import music, error, meta

CONFIG = config.load_config() # load the config file

bot = commands.Bot(command_prefix=CONFIG["prefix"])

@bot.event
async def on_ready():
    logging.info(f"Logged in as {bot.user.name}")

COGS = [
    music.Music,
    error.CommandErrorHandler,
    meta.Meta
]

def add_cogs(bot):
    for cog in COGS:
        bot.add_cog(cog(bot)) # Initialize the cog and add it to the bot

def run():
    add_cogs(bot)
    bot.run(CONFIG["token"])
