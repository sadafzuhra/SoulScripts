
import streamlit as st
import random

# Load quotes from file
with open("quotes.txt", "r", encoding="utf-8") as file:
    quotes = [line.strip() for line in file if line.strip()]

# Select a random quote
random_quote = random.choice(quotes)

# Apply soft journal styling
with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Display the quote
st.markdown("## 🌸 Quote of the Day")
st.success(random_quote)

# Optionally allow users to save their thoughts
st.markdown("### 💭 Your Reflection")
st.text_area("Write what this quote means to you...", height=200)
