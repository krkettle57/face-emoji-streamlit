from io import BytesIO

import streamlit as st
from PIL import Image

from fes.const import EXAMPLE_IMAGE_DIR
from fes.face_annotate import get_image_face_hided_by_emoji
from fes.models import Emoji


def render() -> None:
    st.title("顔を絵文字で隠せるアプリ")

    # 画像アップロード
    user_image_fp = st.file_uploader("画像を選択してください", type=["png", "jpg"])

    # サンプル画像選択
    image_paths = {
        EXAMPLE_IMAGE_DIR.joinpath("man.jpg"): "男性",
        EXAMPLE_IMAGE_DIR.joinpath("woman.jpg"): "女性",
        EXAMPLE_IMAGE_DIR.joinpath("multi.jpg"): "三銃士",
    }
    example_image_fp = st.selectbox(
        "サンプル画像",
        list(image_paths.keys()),
        format_func=lambda x: image_paths[x],
    )

    # 顔文字選択
    emoji = st.selectbox(
        "絵文字",
        list(Emoji),
        format_func=lambda x: f"{x.value} {x.name}",  # x.valueのみだと顔文字が見切れる
    )

    page_left, page_right = st.columns([1, 1])
    page_left.subheader("入力画像")
    page_right.subheader("実行結果")

    image = Image.open(example_image_fp)
    if user_image_fp is not None:
        image = Image.open(user_image_fp)

    page_left.image(image)
    if page_left.button("実行"):
        with st.spinner("実行中..."):
            output = get_image_face_hided_by_emoji(image, emoji)
        page_right.image(output)

        buf = BytesIO()
        image.save(buf, format="PNG")
        byte_im = buf.getvalue()
        page_right.download_button(
            label="ダウンロード",
            data=byte_im,
            file_name="result.png",
            mime="image/png",
        )


if __name__ == "__main__":
    render()
