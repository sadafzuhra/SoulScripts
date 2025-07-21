import streamlit as st
import json
import os
from datetime import date

st.set_page_config(page_title="Inner Child Check-In", page_icon="🧸")



with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

DATA_FILE = "data/soulscripts_data.json"

st.title("🧸 Inner Child Check-In")

# Helpers for loading and saving data
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
today = str(date.today())
today_data = all_data.get(today, {})

feeling = st.text_area("🧠 How is your inner child feeling today?", value=today_data.get("inner_child", {}).get("feeling", ""))
nurture = st.text_area("💞 How did you nurture her today?", value=today_data.get("inner_child", {}).get("nurture", ""))

if st.button("💾 Save Inner Child Check-In"):
    all_data[today] = all_data.get(today, {})
    all_data[today]["inner_child"] = {
        "feeling": feeling,
        "nurture": nurture
    }
    save_data(all_data)
    st.success("✅ Inner child entry saved!")
