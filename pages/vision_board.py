import streamlit as st
import os
from PIL import Image

UPLOAD_FOLDER = "uploads/vision_board"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

st.title("🧠 Vision Board")

# Upload section
uploaded_file = st.file_uploader("Upload your dream image", type=["jpg", "jpeg", "png"])
if uploaded_file:
    file_path = os.path.join(UPLOAD_FOLDER, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success("Image uploaded successfully!")

# Show all uploaded images
st.markdown("### 🌟 Your Vision Board")
image_files = os.listdir(UPLOAD_FOLDER)
for image_name in image_files:
    image_path = os.path.join(UPLOAD_FOLDER, image_name)
    image = Image.open(image_path)
    st.image(image, caption=image_name, use_column_width=True)
