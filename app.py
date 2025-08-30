import streamlit as st
import random

# -------------------------------
# Title & Introduction
# -------------------------------
st.set_page_config(page_title="MindEase Prototype", page_icon="💡", layout="centered")
st.title("💡 MindEase: Your Mental Wellness Buddy")
st.write("A simple prototype to support mental health with **chat**, **daily affirmations**, and **journaling**.")

# -------------------------------
# Feature 1: Chatbot
# -------------------------------
st.header("🗨️ Chat with MindEase")
user_input = st.text_input("How are you feeling today?")
if user_input:
    responses = [
        "I hear you. That sounds tough 💙",
        "You're stronger than you think 🌟",
        "It's okay to take a break, you deserve it 🌼",
        "Thanks for sharing your feelings with me 🤗"
    ]
    st.write("MindEase:", random.choice(responses))

# -------------------------------
# Feature 2: Daily Affirmations
# -------------------------------
st.header("🌸 Daily Affirmation")
affirmations = [
    "I am worthy of love and kindness.",
    "I choose to focus on what I can control.",
    "I am proud of how far I have come.",
    "My feelings are valid and important.",
    "I have the strength to overcome challenges."
]
if st.button("✨ Get Affirmation"):
    st.success(random.choice(affirmations))

# -------------------------------
# Feature 3: Journaling
# -------------------------------
st.header("📖 Daily Journal")
journal_entry = st.text_area("Write your thoughts here:")
if st.button("💾 Save Entry"):
    with open("journal.txt", "a") as f:
        f.write(journal_entry + "\n---\n")
    st.success("Your journal entry has been saved safely! 📝")
