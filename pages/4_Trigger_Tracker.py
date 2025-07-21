import streamlit as st
import json
import os
from datetime import date

st.set_page_config(page_title="Trigger Tracker", page_icon="🚨")


with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

DATA_FILE = "data/soulscripts_data.json"

st.title("🚨 Trigger Tracker & Coping Tools")

# Load & Save Helpers
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

all_data = load_data()
today = str(date.today())
today_data = all_data.get(today, {})

st.subheader("🔁 What triggered you today?")
trigger = st.text_input("Triggering Event", value=today_data.get("trigger", {}).get("event", ""))
emotion = st.selectbox("Emotional Response", ["Anger", "Fear", "Sadness", "Shame", "Anxiety", "Overwhelm", "Other"], index=0)
coping = st.text_area("Coping Mechanism Used", value=today_data.get("trigger", {}).get("coping", ""))

if st.button("💾 Save Trigger Log"):
    all_data[today] = all_data.get(today, {})
    all_data[today]["trigger"] = {
        "event": trigger,
        "emotion": emotion,
        "coping": coping
    }
    save_data(all_data)
    st.success("✅ Trigger log saved!")