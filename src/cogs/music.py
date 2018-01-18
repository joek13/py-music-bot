from discord.ext import commands
import discord
import asyncio
import youtube_dl
import logging
from urllib import request
from state import GuildState
from video import Video

class Music:
    """Bot commands to help play music."""
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    async def leave(self, ctx):
        """Leaves the voice channel, if currently in one."""
        client = ctx.guild.voice_client
        if client and client.channel:
            await client.disconnect()
        else:
            raise commands.CommandError("Not in a voice channel.")


    @commands.command(brief="Plays audio from <url>")
    @commands.guild_only()
    async def play(self, ctx, *, url):
        """Plays audio hosted at <url> (or performs a search for <url> and plays the first result)."""

        client = ctx.guild.voice_client

        if client and client.channel:
            pass
        else:
            if ctx.author.voice != None and ctx.author.voice.channel != None:
                channel = ctx.author.voice.channel
                try:
                    video = Video(url)
                except youtube_dl.DownloadError as e:
                    await ctx.send("There was an error downloading your video, sorry.") 
                    return
                client = await channel.connect()
                source = discord.FFmpegPCMAudio(video.stream_url)
                def after_playing(error):
                    if error:
                        ctx.send(f"Error playing audio: {error}")
                        logging.warn(f"Error playing audio: {error}")
                    asyncio.run_coroutine_threadsafe(client.disconnect(), self.bot.loop)
                client.play(source, after=after_playing)
                await ctx.send("", embed=video.get_embed())
                logging.info(f"Now playing '{video.title}'")
            else:
                raise commands.CommandError("You need to be in a voice channel to do that.")
