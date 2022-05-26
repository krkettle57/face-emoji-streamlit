from enum import Enum, auto
from pathlib import Path

import augly.image as imaugs
import face_recognition
from augly.utils.base_paths import EMOJI_DIR
from PIL import Image

BBox = tuple[int, int, int, int]  # top, right, bottom, left


class SmileysEmoji(Enum):
    grinning_face = auto()


def overlay_emoji(image: Image, face_bbox: BBox, emoji_type: SmileysEmoji) -> Image:
    emoji_path = Path(EMOJI_DIR, "smileys", f"{emoji_type.name}.png")
    W, H = image.size
    top, right, bottom, left = face_bbox

    x_pos, y_pos = float(left) / W, float(top) / H
    emoji_size = max((right - left) / W, (bottom - top) / H)
    emoji_aug = imaugs.OverlayEmoji(emoji_path=emoji_path, opacity=1.0, emoji_size=emoji_size, x_pos=x_pos, y_pos=y_pos)
    overlayed_image = emoji_aug(image)

    return overlayed_image


def face_detection(path: Path) -> list[BBox]:
    image = face_recognition.load_image_file(image_path)
    face_bboxes = face_recognition.face_locations(image)
    # TODO: [int, Any, Any, int]の時の例外処理
    return face_bboxes


if __name__ == "__main__":
    image_path = Path("./images/001_man_ok.jpg")
    face_bboxes = face_detection(image_path)

    overlayed_image = Image.open(image_path)
    for face_bbox in face_bboxes:
        overlayed_image = overlay_emoji(overlayed_image, face_bbox, SmileysEmoji.grinning_face)
    overlayed_image.save("hoge.png")
