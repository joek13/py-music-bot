import discord
from discord.ext import commands

class CommandErrorHandler:
    def __init__(self, bot):
        self.bot = bot

    async def on_command_error(self, ctx, error):
        if hasattr(ctx.command, "on_error"):
            return # Don't interfere with custom error handlers

        error = getattr(error, "original", error) # get original error

        if isinstance(error, commands.CommandInvokeError):
            await ctx.send("There was an unexpected error invoking that command.")
        else:
            return await ctx.send(f"Error executing command `{ctx.command.name}`: {str(error)}")

        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)
