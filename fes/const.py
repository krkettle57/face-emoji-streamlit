from pathlib import Path

FONT_URL = "https://github.com/googlefonts/noto-emoji/raw/main/fonts/NotoColorEmoji.ttf"
DATA_DIR = Path(__file__).parent.parent.resolve().joinpath("data")
FONT_DIR = DATA_DIR.joinpath("fonts")
NOTE_EMOJI_FONT_FILEPATH = DATA_DIR.joinpath("fonts/NotoColorEmoji.ttf")
EMOJI_IMAGE_DIR = DATA_DIR.joinpath("images/emoji")
EXAMPLE_IMAGE_DIR = DATA_DIR.joinpath("images/example")
