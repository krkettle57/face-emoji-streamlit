import os

import augly.image as imaugs
from augly.utils.base_paths import EMOJI_DIR
from PIL import Image


def main():
    im_path = "./data/images/man1.jpg"
    im = Image.open(im_path).convert("RGB")

    emoji_category = [
        "activity",
        "alphanumeric",
        "animals_and_nature",
        "flags",
        "food_and_drink",
        "objects",
        "people",
        "smileys",
        "symbols",
        "travel_and_places",
    ]

    x, y = (0.8, 0.8)
    opacity = 0.7
    emoji_size = 0.2

    for c in emoji_category:
        emoji_dir = os.path.join(EMOJI_DIR, c)
        emoji_aug = imaugs.RandomEmojiOverlay(
            emoji_directory=emoji_dir, opacity=opacity, emoji_size=emoji_size, x_pos=x, y_pos=y
        )
        new_im = emoji_aug(im)
        new_im.save(f"cat-emoji-{c}.jpg")


if __name__ == "__main__":
    main()
