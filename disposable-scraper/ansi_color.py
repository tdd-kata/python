# https://stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal#answer-287944
# https://en.wikipedia.org/wiki/ANSI_escape_code#Colors
class ANSIColorEscapeSequence:
    # 3-bit 8-colors
    # https://en.wikipedia.org/wiki/ANSI_escape_code#3-bit_and_4-bit
    # ESC[⟨n⟩m
    BRIGHT_BLACK = '\033[0m'
    BRIGHT_RED = '\033[91m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_BLUE = '\033[94m'
    BRIGHT_MAGENTA = '\033[95m'
    BRIGHT_CYAN = '\033[96m'
    BRIGHT_WHITE = '\033[97m'

    # 8-bit 256-colors
    # https://en.wikipedia.org/wiki/ANSI_escape_code#8-bit
    # ESC[38:5:⟨n⟩m Select foreground color
    # ESC[48:5:⟨n⟩m Select background color
    HIGH_INTENSITY_BLACK = '\033[38:5:8m'
    HIGH_INTENSITY_RED = '\033[38:5:9m'
    HIGH_INTENSITY_GREEN = '\033[38:5:10m'
    HIGH_INTENSITY_YELLOW = '\033[38:5:11m'
    HIGH_INTENSITY_BLUE = '\033[38:5:12m'
    HIGH_INTENSITY_MAGENTA = '\033[38:5:13m'
    HIGH_INTENSITY_CYAN = '\033[38:5:14m'
    HIGH_INTENSITY_WHITE = '\033[38:5:15m'

    # 24-bit 16 million colors
    # https://en.wikipedia.org/wiki/ANSI_escape_code#24-bit
    # ESC[38;2;⟨r⟩;⟨g⟩;⟨b⟩m Select RGB foreground color
    # ESC[48;2;⟨r⟩;⟨g⟩;⟨b⟩m Select RGB background color
    AMBER = '\033[38;2;255;135;0m'


def error(message: str):
    print(
        f"{ANSIColorEscapeSequence.HIGH_INTENSITY_RED}"
        f"{message}"
        f"{ANSIColorEscapeSequence.BRIGHT_BLACK}"
    )


def info(message: str):
    print(f"{message}")


def debug(message: str):
    print(
        f"{ANSIColorEscapeSequence.HIGH_INTENSITY_MAGENTA}"
        f"{message}"
        f"{ANSIColorEscapeSequence.BRIGHT_BLACK}"
    )


def meta(message: str):
    print(
        f"{ANSIColorEscapeSequence.AMBER}"
        f"{message}"
        f"{ANSIColorEscapeSequence.BRIGHT_BLACK}"
    )
