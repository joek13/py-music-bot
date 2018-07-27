from discord.ext import commands
import discord
from datetime import datetime
import util


class Meta:
    """Commands relating to the bot itself."""

    def __init__(self, bot, config):
        self.bot = bot
        self.start_time = datetime.now()
        self.config = config
        bot.remove_command("help")

    @commands.command(name="help")
    async def _help(self, ctx, command: str = None):
        """Gets help for a single command, or an entire category."""
        formatter = commands.HelpFormatter(show_check_failure=True)
        if command is None:
            await ctx.send("\n".join(await formatter.format_help_for(
                ctx, self.bot)))
        else:
            thing = self.bot.get_cog(command) or self.bot.get_command(command)
            if thing is None:
                await ctx.send(f"Command or category {command} not found.")
            else:
                await ctx.send("\n".join(await formatter.format_help_for(
                    ctx, thing)))

    @commands.command()
    async def uptime(self, ctx):
        """Tells how long the bot has been running."""
        uptime_seconds = round(
            (datetime.now() - self.start_time).total_seconds())
        await ctx.send(f"Current Uptime: {util.format_seconds(uptime_seconds)}"
                       )
