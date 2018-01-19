from discord.ext import commands
import discord
import asyncio
import youtube_dl
import logging
from urllib import request
from video import Video

async def audio_playing(ctx):
    """Checks that audio is currently playing before continuing."""
    client = ctx.guild.voice_client
    if client and client.channel and client.source:
        return True
    else:
        raise commands.CommandError("Not currently playing any audio.")
class Music:
    """Bot commands to help play music."""
    def __init__(self, bot):
        self.bot = bot
        self.states = {}

    def get_state(self, guild):
        """Gets the state for `guild`, creating it if it does not exist."""
        if guild.id in self.states:
            return self.states[guild.id]
        else:
            self.states[guild.id] = GuildState()
            return self.states[guild.id]

    @commands.command()
    @commands.guild_only()
    async def leave(self, ctx):
        """Leaves the voice channel, if currently in one."""
        client = ctx.guild.voice_client
        if client and client.channel:
            await client.disconnect()
        else:
            raise commands.CommandError("Not in a voice channel.")


    @commands.command(aliases=["resume", "p"])
    @commands.guild_only()
    @commands.check(audio_playing)
    async def pause(self, ctx):
        """Pauses any currently playing audio."""
        client = ctx.guild.voice_client

        if client.is_paused():
            client.resume()
            await ctx.send("▶️")
        else:
            client.pause()
            await ctx.send("⏸️")

    @commands.command(aliases=["vol", "v"])
    @commands.guild_only()
    @commands.check(audio_playing)
    async def volume(self, ctx, volume: int):
        """Change the volume of currently-playing audio (values 0-250)"""
        state = self.get_state(ctx.guild)

        # clamp volume to [0, 250]
        if volume < 0:
            volume = 0
        elif volume > 250:
            volume = 250

        client = ctx.guild.voice_client

        state.volume = float(volume) / 100.0
        client.source.volume = state.volume # update the AudioSource's volume to match
        
    @commands.command(brief="Plays audio from <url>.")
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
                state = self.get_state(ctx.guild) # get the guild's state
                source = discord.PCMVolumeTransformer(
                            discord.FFmpegPCMAudio(video.stream_url),
                            volume=state.volume)
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

class GuildState:
    """Helper class managing per-guild state."""
    def __init__(self):
        self.volume = 1.0
