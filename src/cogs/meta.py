from discord.ext import commands
import discord

class Meta:
    """Commands relating to the bot itself."""
    def __init__(self, bot):
        self.bot = bot
        bot.remove_command("help")

    @commands.command(name="help")
    async def _help(self, ctx, command: str = None):
        """Gets help for a single command, or an entire category."""
        formatter = commands.HelpFormatter(show_check_failure=True)
        if command is None:
            await ctx.send("\n".join(await formatter.format_help_for(ctx, self.bot)))
        else:
            thing = self.bot.get_cog(command) or self.bot.get_command(command)
            if thing is None:
                await ctx.send(f"Command or category {command} not found.")
            else:
                await ctx.send("\n".join(await formatter.format_help_for(ctx, thing)))
