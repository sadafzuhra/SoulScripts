
import streamlit as st
from datetime import datetime

st.set_page_config(page_title="SoulScripts Journal", page_icon="🌸", layout="centered")

st.markdown("""
<style>
    .main {background-color: #fdf0e6;}
    h1, h2, h3 {color: #d48a8a; font-family: 'Georgia'}
</style>
""", unsafe_allow_html=True)

st.title("🌸 SoulScripts: Growth & Healing Journal")

st.markdown("""
Welcome to your personal digital journal inspired by *Obsessed with Growth*. Use the sidebar to navigate through your journey of reflection, clarity, and healing.

> *“Growth is a choice we make daily.”*

---

**Quick Links:**
- Morning & Evening Journals
- Weekly and Monthly Reflections
- Trigger and Dream Tracker
- Vision Board & Quotes
- Inner Child Check-in

""")

try:
    st.image("assets/pastel_backgrounds/cover.jpg", use_column_width=True)
except:
    st.warning("📷 Cover image not found. Please add 'cover.jpg' to assets/pastel_backgrounds/.")

st.info(f"📅 Today's Date: {datetime.now().strftime('%B %d, %Y')}")
