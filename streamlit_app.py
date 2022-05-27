from pathlib import Path

import face_recognition
from PIL import Image

from const import EMOJI_IMAGE_DIR, EXAMPLE_IMAGE_DIR
from models import Emoji
from type import BBox


def get_emoji_size(bbox: BBox) -> int:
    top, right, bottom, left = bbox
    size = max(bottom - top, right - left)
    return size


def get_emoji_position(bbox: BBox) -> tuple[int, int]:
    top, _, _, left = bbox
    return (left, top)


def draw_emoji(im: Image, emoji: Emoji, size: int, pos: tuple[int, int]) -> None:
    emoji_path = EMOJI_IMAGE_DIR.joinpath(f"{emoji.name}.png")
    emoji_im = Image.open(emoji_path).convert("RGBA").resize((size, size))
    im.paste(emoji_im, pos, emoji_im)


def face_detection(image_path: Path) -> list[BBox]:
    image = face_recognition.load_image_file(image_path)
    face_bboxes = face_recognition.face_locations(image)
    # TODO: [int, Any, Any, int]の時の例外処理
    return face_bboxes


if __name__ == "__main__":
    image_path = EXAMPLE_IMAGE_DIR.joinpath("man.jpg")
    face_bboxes = face_detection(image_path)

    image = Image.open(image_path)
    for face_bbox in face_bboxes:
        size = get_emoji_size(face_bbox)
        pos = get_emoji_position(face_bbox)
        draw_emoji(image, Emoji.grinning, size, pos)
    image.save("hoge.png")
