import youtube_dl as ytdl
import discord

YTDL_OPTS = {
        "default_search": "ytsearch",
        "format": "bestaudio/best",
        "quiet": True
}

class Video:
    """Class containing information about a particular video."""
    def __init__(self, url_or_search):
        """Plays audio from (or searches for) a URL."""
        with ytdl.YoutubeDL(YTDL_OPTS) as ydl:
            info = ydl.extract_info(url_or_search, download=False)
            video = None
            if "_type" in info and info["_type"] == "playlist":
                video = info["entries"][0]
            else:
                video = info
            video_format = video["formats"][0]
            self.stream_url = video_format["url"]
            self.video_url = video["webpage_url"]
            self.title = video["title"]
            self.uploader = video["uploader"]
            self.thumbnail = video["thumbnail"] if "thumbnail" in video else None
    def get_embed(self):
        """Makes an embed out of this Video's information."""
        embed = discord.Embed(
            title=self.title,
            description=self.uploader,
            url=self.video_url)
        if self.thumbnail:
            embed.set_thumbnail(url=self.thumbnail)
        return embed
