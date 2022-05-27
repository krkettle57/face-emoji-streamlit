import urllib.request
from pathlib import Path

FONT_URL = "https://github.com/googlefonts/noto-emoji/raw/main/fonts/NotoColorEmoji.ttf"

data = urllib.request.urlopen(FONT_URL).read()
savedir = Path(__file__).parent.resolve().joinpath("data/fonts/")
savedir.mkdir(exist_ok=True)
savedir.joinpath("NotoColorEmoji.ttf").write_bytes(data)
