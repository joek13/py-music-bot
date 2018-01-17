from discord.ext import commands
from state import GuildState

STATES = []

class Music:
    """Bot commands to help play music."""
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    @commands.guild_only()
    async def play(self, ctx, url):
        """Plays audio hosted at <url>."""
        if ctx.guild.id in STATES:
            pass
        else:
            if ctx.author.voice != None and ctx.author.voice.channel != None:
                channel = ctx.author.voice.channel
            else:
                raise commands.CommandError("You need to be in a voice channel to do that.")
