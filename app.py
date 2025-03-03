import streamlit as st
import random

# Initialize session state (to keep the number same)
if 'random_number' not in st.session_state:
    st.session_state.random_number = random.randint(1, 100)

if 'attempts' not in st.session_state:
    st.session_state.attempts = 0

# Set Page Configuration
st.set_page_config(page_title="Guess The Number Game", page_icon="🎲", layout="centered")

# Game Header
st.markdown("<h1 style='text-align: center; color: #FF5733;'>🎯 Guess the Number Game 🎲</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: #3498db;'>I have chosen a number between <b>1 and 100</b>. Can you guess it?</h4>", unsafe_allow_html=True)

# User Input
user_guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)

# Check Guess Button
if st.button("✅ Check Guess"):
    st.session_state.attempts += 1  # Count attempts
    
    # Compare the guess with the actual number
    if user_guess < st.session_state.random_number:
        st.warning("❌ Too low! Try again. 🔽")
    elif user_guess > st.session_state.random_number:
        st.warning("❌ Too high! Try again. 🔼")
    else:
        st.success(f"🎉 Congratulations! You guessed the number {st.session_state.random_number} correctly in {st.session_state.attempts} attempts! 🎯")
        st.session_state.random_number = random.randint(1, 100)  # Reset game after correct guess
        st.session_state.attempts = 0  # Reset attempt count

# Restart Game Button
if st.button("🔄 Restart Game"):
    st.session_state.random_number = random.randint(1, 100)  # New number
    st.session_state.attempts = 0  # Reset attempts
    st.rerun()
