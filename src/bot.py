import discord
import logging
import sys
from discord.ext import commands
from discord.voice_client import VoiceClient
from cogs import music, error, meta, tips
import config

cfg = config.load_config()

bot = commands.Bot(command_prefix=cfg["prefix"])


@bot.event
async def on_ready():
    logging.info(f"Logged in as {bot.user.name}")
    print("ready")
@bot.command(pass_context=True)
async def join(ctx):
    destination = ctx.author.voice.channel
    #if ctx.voice_state.voice:
    #    await ctx.voice_state.voice.move_to(destination)
    #    return

    ctx.voice_state.voice = await destination.connect()


    

COGS = [music.Music, error.CommandErrorHandler, meta.Meta, tips.Tips]


def add_cogs(bot):
    for cog in COGS:
        print(str(type(cog)))
        bot.add_cog(cog(bot, cfg))  # Initialize the cog and add it to the bot


def run():
    add_cogs(bot)
    if cfg["token"] == "":
        raise ValueError(
            "No token has been provided. Please ensure that config.toml contains the bot token."
        )
        sys.exit(1)
    bot.run(cfg["token"])
run();