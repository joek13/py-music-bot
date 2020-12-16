# discord.py MusicBot

A simple musicbot written in Discord.py that utilizes YoutubeDL and ffmpeg to stream audio. Use the `help` command to get a list of commands!

## Additional Dependencies

Make sure that [pipenv](https://pipenv.pypa.io/en/latest/) is installed. Navigate to the project directory, and run `pipenv install` to install the Python dependencies.

To allow for streaming of media, make sure `opus` and `ffmpeg` are installed and in your environment.

To run the bot, activate the virtual environment with `pipenv shell` and then `python src/main.py` to start the bot.

## Configuring

When you run the bot for the first time, a default configuration file will be generated called `config.toml`. You can enter that file and add your token, etc.

If you ever wish to restore the bot to default configuration, you can simply delete (or rename) your config file. A new one will be generated upon startup.
