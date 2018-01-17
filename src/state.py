class GuildState:
    """State object that is maintained per-guild. Holds information about currently playing music as well as a reference to the VoiceState (if applicable)."""

    def __init__(self):
        self.voice_state = None
