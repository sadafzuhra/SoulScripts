import streamlit as st
import json
import os
from datetime import date

st.set_page_config(page_title="Weekly Reflection", page_icon="📆")


with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

DATA_FILE = "data/soulscripts_data.json"

st.title("📆 Weekly Reflection")
st.markdown("Reflect on the highs, lows, and lessons of this past week.")

# Load existing data
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

all_data = load_data()
this_week = f"week-{date.today().isocalendar().week}-{date.today().year}"
week_data = all_data.get(this_week, {})

wins = st.text_area("✨ Wins of the Week", value=week_data.get("wins", ""))
challenges = st.text_area("⚡ Challenges Faced", value=week_data.get("challenges", ""))
selfcare = st.slider("🧘 Self-Care Rating (1 = Low, 10 = High)", 1, 10, week_data.get("selfcare", 5))

if st.button("💾 Save Weekly Reflection"):
    all_data[this_week] = {
        "wins": wins,
        "challenges": challenges,
        "selfcare": selfcare
    }
    save_data(all_data)
    st.success("✅ Weekly reflection saved!")
