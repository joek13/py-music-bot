import discord, sys, traceback, logging
from discord.ext import commands

class CommandErrorHandler:
    def __init__(self, bot):
        self.bot = bot

    async def on_command_error(self, ctx, error):
        if hasattr(ctx.command, "on_error"):
            return # Don't interfere with custom error handlers

        error = getattr(error, "original", error) # get original error

        if isinstance(error, commands.CommandError):
            return await ctx.send(f"Error executing command `{ctx.command.name}`: {str(error)}")

        await ctx.send("An unexpected error occurred while running that command.")
        logging.warn("Ignoring exception in command {}:".format(ctx.command))
        logging.warn("\n"+"".join(traceback.format_exception(type(error), error, error.__traceback__)))
