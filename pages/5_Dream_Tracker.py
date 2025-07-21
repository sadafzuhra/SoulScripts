import streamlit as st
import json
import os
from datetime import date

st.set_page_config(page_title="Dream Tracker", page_icon="💤")


with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

DATA_FILE = "data/soulscripts_data.json"

st.title("💤 Dream Tracker")

# Helpers for loading and saving data
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

# Load existing data
all_data = load_data()
today = str(date.today())
today_data = all_data.get(today, {})

description = st.text_area("📝 Dreams Remembered", value=today_data.get("dream", {}).get("description", ""))
symbols = st.text_input("🔮 Symbols or Details Noticed", value=", ".join(today_data.get("dream", {}).get("symbols", [])))
feeling = st.selectbox("🌙 Feeling from the Dream", ["Peaceful", "Confused", "Fearful", "Excited", "Sad", "Other"])

if st.button("💾 Save Dream Log"):
    all_data[today] = all_data.get(today, {})
    all_data[today]["dream"] = {
        "description": description,
        "symbols": [s.strip() for s in symbols.split(",") if s.strip()],
        "emotion": feeling
    }
    save_data(all_data)
    st.success("✅ Dream entry saved!")
