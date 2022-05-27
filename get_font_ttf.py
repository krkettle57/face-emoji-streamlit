import urllib.request

from const import NOTE_EMOJI_FONT_FILEPATH

FONT_URL = "https://github.com/googlefonts/noto-emoji/raw/main/fonts/NotoColorEmoji.ttf"

data = urllib.request.urlopen(FONT_URL).read()
NOTE_EMOJI_FONT_FILEPATH.parent.resolve().mkdir(exist_ok=True)
NOTE_EMOJI_FONT_FILEPATH.write_bytes(data)
