from enum import Enum
from pathlib import Path

import face_recognition
from PIL import Image, ImageDraw, ImageFont

from const import NOTE_EMOJI_FONT_FILEPATH

BBox = tuple[int, int, int, int]  # top, right, bottom, left


class Emoji(Enum):
    grinning = "😀"
    pleading_face = "🥺"


def get_emoji_size(bbox: BBox) -> int:
    top, right, bottom, left = bbox
    size = max(bottom - top, right - left)
    return size


def get_emoji_position(bbox: BBox) -> tuple[int, int]:
    top, right, bottom, left = bbox
    return (left, top)


def draw_emoji(image: Image, emoji: Emoji, size: int, pos: tuple[int, int]) -> None:
    unicode_text = emoji.value
    font = ImageFont.truetype(str(NOTE_EMOJI_FONT_FILEPATH), 109)
    draw = ImageDraw.Draw(image)
    draw.text(pos, unicode_text, font=font, embedded_color=True)


def face_detection(path: Path) -> list[BBox]:
    image = face_recognition.load_image_file(image_path)
    face_bboxes = face_recognition.face_locations(image)
    # TODO: [int, Any, Any, int]の時の例外処理
    return face_bboxes


if __name__ == "__main__":
    image_path = Path("./data/images/friends.jpg")
    face_bboxes = face_detection(image_path)

    image = Image.open(image_path)
    for face_bbox in face_bboxes:
        size = get_emoji_size(face_bbox)
        pos = get_emoji_position(face_bbox)
        draw_emoji(image, Emoji.grinning, size, pos)
    image.save("hoge.png")
