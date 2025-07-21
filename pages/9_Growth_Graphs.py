import streamlit as st
import json
import os
import matplotlib.pyplot as plt
from datetime import datetime

st.set_page_config(page_title="Growth Graphs", page_icon="📊")


with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

DATA_FILE = "data/soulscripts_data.json"

st.title("📊 Growth Graphs")

# Load data
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}

data = load_data()

# Extract self-care scores by week
weeks = []
scores = []

for k, v in data.items():
    if k.startswith("week_"):
        date_str = k.replace("week_", "")
        dt = datetime.strptime(date_str, "%Y-%m-%d")
        rating = v.get("weekly", {}).get("self_care")
        if rating is not None:
            weeks.append(dt.strftime("%b %d"))
            scores.append(rating)

if weeks:
    st.subheader("💖 Self-Care Rating Over Time")
    fig, ax = plt.subplots()
    ax.plot(weeks, scores, marker='o', color='#d48a8a')
    ax.set_ylabel("Rating (0-10)")
    ax.set_xlabel("Week Start")
    ax.set_title("Your Weekly Self-Care Score")
    st.pyplot(fig)
else:
    st.info("Not enough data to display graphs yet. Try filling in your weekly reflections!")
