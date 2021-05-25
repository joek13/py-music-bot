# discord.py MusicBot

A simple, unintrusive musicbot written in Discord.py that utilizes YoutubeDL and ffmpeg to stream audio. Use the `help` command to get a list of commands!

## Getting started
If you just want to get up and running with the bot quickly:

1. Clone this repository using the GitHub website or GitHub/git CLI.
2. Install `pipenv`, the Python dependency manager, if necessary. Also, ensure `opus` and `ffmpeg` are installed on your machine and available in your environment. Both are used for media streaming.
3. Navigate into the project directory and run `pipenv install` to install dependencies.
4. Activate the Pipenv using `pipenv shell`. Run the bot using `python -m musicbot`.
5. On first startup, a default `config.toml` will be generated without an API token, so the bot will abort complaining that `No token has been provided.` Fill your bot's token into `config.toml`.
6. Use something like the [Discord API Permissions calculator](https://discordapi.com/permissions.html) to generate an invite link and invite your bot to your server, if necessary.
7. Run the bot using `python -m musicbot`.

## Additional Dependencies

Make sure that [pipenv](https://pipenv.pypa.io/en/latest/) is installed. Navigate to the project directory, and run `pipenv install` to install the Python dependencies.

To allow for streaming of media, make sure `opus` and `ffmpeg` are installed and in your environment.

To run the bot, activate the virtual environment with `pipenv shell` and then `python -m musicbot` to start the bot.

## Configuring

When you run the bot for the first time, a default configuration file will be generated called `config.toml`. You can enter that file and add your token, etc. The default file looks like this:

```toml
"token"="" # the bot's token
"prefix"="!" # prefix used to denote commands

[music]
# Options for the music commands
"max_volume"=250 # Max audio volume. Set to -1 for unlimited.
"vote_skip"=true # whether vote-skipping is enabled
"vote_skip_ratio"=0.5 # the minimum ratio of votes needed to skip a song
[tips]
"github_url"="https://github.com/joek13/py-music-bot"
```

If you ever wish to restore the bot to default configuration, you can simply delete (or rename) your config file. A new one will be generated upon startup.

## Commands
From the bot's `help` command:
```
Meta:
  uptime Tells how long the bot has been running.
Music:
  leave  Leaves the voice channel, if currently in one.
  play   Plays audio from <url>.
Tips:
  tip    Get a random tip about using the bot.
​No Category:
  help   Shows this message
```

## Contributing
Issues and pull requests are welcomed and appreciated. I can't guarantee that I will respond to all issues in a timely manner, but I will try my best to respond to any issues that arise.