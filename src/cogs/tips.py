from discord.ext import commands
import discord
import random

TIPS = ["Only admins and the song requester can immediately skip songs. Everybody else will have to vote!", ""]

class Tips:
    """Commands for providing tips about using the bot."""

    def __init__(self, bot, config):
        self.bot = bot
        self.config = config[__name__.split(".")[-1]]

    @commands.command()
    async def tip(self, ctx):
        """Get a random tip about using the bot."""
        index = random.randrange(len(TIPS))
        await ctx.send(f"**Tip #{index+1}:** {TIPS[index]}")
