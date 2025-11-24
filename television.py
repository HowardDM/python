class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        """Set TV off, unmuted, min volume and channel."""
        self.__status = False
        self.__muted = False
        self.__channel = Television.MIN_CHANNEL
        self.__volume = Television.MIN_VOLUME

    def power(self):
        """Turn TV on/off."""
        self.__status = not self.__status

    def mute(self):
        """Mute/unmute TV if it's on."""
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self):
        """Go to next channel, wrap around if needed."""
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self):
        """Go to previous channel, wrap around if needed."""
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self):
        """Increase volume, unmute if muted."""
        if self.__status:
            self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self):
        """Decrease volume, unmute if muted."""
        if self.__status:
            self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self):
        """Show TV status, channel, and volume (0 if muted)."""
        if self.__status:
            vol = 0 if self.__muted else self.__volume
            return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {vol}"
        else:
            return "TV is off"