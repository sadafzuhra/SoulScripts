import streamlit as st
import os
from datetime import date

st.set_page_config(page_title="Vision Board", page_icon="🌠")


with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

UPLOAD_FOLDER = "uploads/vision_board"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

st.title("🌠 Vision Board")

st.markdown("Upload and view images that represent your goals and dreams.")

uploaded_files = st.file_uploader("📷 Upload images", accept_multiple_files=True, type=["png", "jpg", "jpeg"])

if uploaded_files:
    for file in uploaded_files:
        save_path = os.path.join(UPLOAD_FOLDER, file.name)
        with open(save_path, "wb") as f:
            f.write(file.getbuffer())
    st.success("Images uploaded!")

st.markdown("---")
st.subheader("🖼️ Your Vision Board")

images = [img for img in os.listdir(UPLOAD_FOLDER) if img.endswith((".jpg", ".jpeg", ".png"))]

cols = st.columns(3)
for i, image in enumerate(images):
    with cols[i % 3]:
        st.image(os.path.join(UPLOAD_FOLDER, image), use_column_width=True)
