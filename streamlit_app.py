import streamlit as st
from PIL import Image

from fes.const import EXAMPLE_IMAGE_DIR
from fes.face_annotate import get_image_face_hided_by_emoji
from fes.models import Emoji


def example_page() -> None:
    st.title("顔を絵文字で隠せるアプリ")
    image_paths = {
        EXAMPLE_IMAGE_DIR.joinpath("man.jpg"): "男性",
        EXAMPLE_IMAGE_DIR.joinpath("woman.jpg"): "女性",
        EXAMPLE_IMAGE_DIR.joinpath("multi.jpg"): "三銃士",
    }
    image_path = st.selectbox(
        "サンプル画像",
        list(image_paths.keys()),
        format_func=lambda x: image_paths[x],
    )

    emoji = st.selectbox(
        "顔文字",
        list(Emoji),
        format_func=lambda x: f"{x.value} {x.name}",  # x.valueのみだと顔文字が見切れる
    )

    page_left, page_right = st.columns([1, 1])
    page_left.subheader("入力画像")
    page_right.subheader("実行結果")

    if image_path is not None:
        image = Image.open(image_path)
        page_left.image(image)

    if page_left.button("実行"):
        with st.spinner("実行中..."):
            output = get_image_face_hided_by_emoji(image_path, emoji)
        page_right.image(output)


if __name__ == "__main__":
    example_page()
