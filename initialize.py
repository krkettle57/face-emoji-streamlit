import urllib.request

from PIL import Image, ImageDraw, ImageFont
from PIL.ImageFont import FreeTypeFont

from fes.const import EMOJI_IMAGE_DIR, FONT_DIR, FONT_URL, NOTE_EMOJI_FONT_FILEPATH
from fes.models import Emoji


def get_font_ttf() -> None:
    data = urllib.request.urlopen(FONT_URL).read()
    FONT_DIR.mkdir(exist_ok=True)
    NOTE_EMOJI_FONT_FILEPATH.write_bytes(data)


def _create_emoji_image(font: FreeTypeFont, emoji: Emoji) -> Image:
    back_ground_color = (255, 0, 0, 0)
    im = Image.new("RGBA", (128, 128), back_ground_color)
    draw = ImageDraw.Draw(im)
    draw.ellipse((25, 25, 75, 75), fill=(255, 0, 0))
    w, h = draw.textsize(emoji.value, font=font)
    draw.text((int((128 - w) / 2), int((128 - h) / 2)), emoji.value, font=font, embedded_color=True)
    return im


def create_emoji_images() -> None:
    font = ImageFont.truetype(str(NOTE_EMOJI_FONT_FILEPATH), 109)
    EMOJI_IMAGE_DIR.mkdir(exist_ok=True)
    for emoji in Emoji:
        im = _create_emoji_image(font, emoji)
        im.save(EMOJI_IMAGE_DIR.joinpath(f"{emoji.name}.png"))


if __name__ == "__main__":
    get_font_ttf()
    create_emoji_images()
