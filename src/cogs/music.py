from discord.ext import commands

class Music:
    """Bot commands to help play music."""
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def test(self, ctx, response):
        """Just a test command."""
        await ctx.send(f"You said: \"{response}\"")
