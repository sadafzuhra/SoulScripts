import streamlit as st
import json
import os
from datetime import date

st.set_page_config(page_title="Quote of the Day", page_icon="📖")
st.title("Quote of the Day")

with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

DATA_FILE = "data/soulscripts_data.json"
QUOTE_FILE = "assets/quotes.txt"

st.title("📖 Quote of the Day")

# Helpers
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def load_quotes():
    if os.path.exists(QUOTE_FILE):
        with open(QUOTE_FILE, "r") as f:
            return [line.strip() for line in f.readlines() if line.strip()]
    return []

# Load everything
all_data = load_data()
today = str(date.today())
quote = all_data.get(today, {}).get("quote", "")

st.text_area("💬 Enter or paste your favorite quote today:", value=quote, key="quote_input")

if st.button("💾 Save Quote"):
    all_data[today] = all_data.get(today, {})
    all_data[today]["quote"] = st.session_state.quote_input
    save_data(all_data)
    st.success("✅ Quote saved!")

if st.button("🎲 Get Random Quote"):
    quotes = load_quotes()
    if quotes:
        st.info(f"✨ *{quotes[0]}*")
    else:
        st.warning("No quotes found. Add some in assets/quotes.txt")
