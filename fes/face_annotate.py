from pathlib import Path
from typing import IO, Union

import face_recognition
from PIL import Image

from fes.const import EMOJI_IMAGE_DIR
from fes.models import Emoji
from fes.type import BBox


def get_emoji_size(bbox: BBox) -> int:
    top, right, bottom, left = bbox
    size = max(bottom - top, right - left)
    return size


def get_emoji_position(bbox: BBox) -> tuple[int, int]:
    top, _, _, left = bbox
    return (left, top)


def draw_emoji(im: Image, emoji: Emoji, size: int, pos: tuple[int, int]) -> None:
    emoji_path = EMOJI_IMAGE_DIR.joinpath(f"{emoji.name}.png")
    emoji_im = Image.open(emoji_path).resize((size, size))
    im.paste(emoji_im, pos, emoji_im)


def face_detection(fp: Union[Path, IO]) -> list[BBox]:
    image = face_recognition.load_image_file(fp)
    face_bboxes = face_recognition.face_locations(image)
    # TODO: [int, Any, Any, int]の時の例外処理
    return face_bboxes


def get_image_face_hided_by_emoji(fp: Union[Path, IO], emoji: Emoji) -> Image:
    face_bboxes = face_detection(fp)
    image = Image.open(fp)
    for face_bbox in face_bboxes:
        size = get_emoji_size(face_bbox)
        pos = get_emoji_position(face_bbox)
        draw_emoji(image, emoji, size, pos)

    return image
