import streamlit as st
import json
import os
from datetime import date

st.set_page_config(page_title="Monthly Review", page_icon="🗓️")


with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

DATA_FILE = "data/soulscripts_data.json"

st.title("🗓️ Monthly Review")
st.markdown("Reflect on your growth moments and lessons this month.")

# Helpers
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

# Load data
all_data = load_data()
month_key = f"month-{date.today().month}-{date.today().year}"
month_data = all_data.get(month_key, {})

highlights = st.text_area("🌟 Monthly Highlights", value=month_data.get("highlights", ""))
lessons = st.text_area("📚 Lessons Learned", value=month_data.get("lessons", ""))
growth = st.text_area("🌱 Growth Moments", value=month_data.get("growth", ""))

if st.button("💾 Save Monthly Review"):
    all_data[month_key] = {
        "highlights": highlights,
        "lessons": lessons,
        "growth": growth
    }
    save_data(all_data)
    st.success("✅ Monthly review saved!")

