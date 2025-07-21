
import streamlit as st
import json
import os
from datetime import date

st.set_page_config(page_title="Daily Journal", page_icon="📝")

with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

DATA_FILE = "data/soulscripts_data.json"


st.title("📝 Daily Journal")
st.markdown("Today’s reflection space for your growth journey.")

# Load existing data or start fresh
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

st.subheader("🌞 Morning Clarity")
intentions = st.text_area("Intentions for the day", value=today_data.get("morning", {}).get("intentions", ""))
affirmations = st.text_area("Positive affirmations", value=today_data.get("morning", {}).get("affirmations", ""))
non_negotiables = st.text_area("Non-negotiables", value=today_data.get("morning", {}).get("non_negotiables", ""))

st.markdown("---")
st.subheader("🌙 Evening Reflection")
went_well = st.text_area("What went well today?", value=today_data.get("evening", {}).get("went_well", ""))
learned = st.text_area("What did you learn today?", value=today_data.get("evening", {}).get("learned", ""))
improve = st.text_area("What will you improve?", value=today_data.get("evening", {}).get("improve", ""))

if st.button("💾 Save Today’s Entry"):
    all_data[today] = all_data.get(today, {})
    all_data[today]["morning"] = {
        "intentions": intentions,
        "affirmations": affirmations,
        "non_negotiables": non_negotiables
    }
    all_data[today]["evening"] = {
        "went_well": went_well,
        "learned": learned,
        "improve": improve
    }
    save_data(all_data)
    st.success("✅ Journal entry saved!")

