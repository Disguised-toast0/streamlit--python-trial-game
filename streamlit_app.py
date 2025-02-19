import streamlit as st
import random
import time

st.title("🐍💦🔫 Snake, Water, Gun Game")
choices = {"snake": "🐍", "water": "💦", "gun": "🔫"}

st.write("### Choose your move:")
col1, col2, col3 = st.columns(3)

user_choice = None

with col1:
    if st.button("🐍 Snake", use_container_width=True):
        user_choice = "snake"
with col2:
    if st.button("💦 Water", use_container_width=True):
        user_choice = "water"
with col3:
    if st.button("🔫 Gun", use_container_width=True):
        user_choice = "gun"


if user_choice:
    thinking_placeholder = st.empty()
    choice_placeholder = st.empty()
    result_placeholder = st.empty()

    thinking_placeholder.markdown("<p style='text-align:center; font-size: 30px;'>🤔 Computer is thinking...</p>", unsafe_allow_html=True)
    time.sleep(1.5)  

    computer_choice = random.choice(list(choices.keys()))
    thinking_placeholder.empty()  

 
    choice_placeholder.markdown(f"""
        <div style='text-align:center; font-size: 30px;'>
            <b>You Chose:</b> {choices[user_choice]} {user_choice.capitalize()} <br>
            <b>Computer Chose:</b> {choices[computer_choice]} {computer_choice.capitalize()}
        </div>
    """, unsafe_allow_html=True)
    
    time.sleep(0.2) 

    if user_choice == computer_choice:
        result_placeholder.markdown("<p style='text-align:center; color:orange; font-size: 40px; '>🤝 It's a Draw! shit! 🤝 </p>", unsafe_allow_html=True)
    elif (user_choice == "snake" and computer_choice == "water") or \
         (user_choice == "water" and computer_choice == "gun") or \
         (user_choice == "gun" and computer_choice == "snake"):
        result_placeholder.markdown("<p style='text-align:center; color:green; font-size: 40px;'>🎉 You Won! Damn 🤬</p>", unsafe_allow_html=True)
    else:
        result_placeholder.markdown("<p style='text-align:center; color:red; font-size: 40px;'>😈 Computer Wins! Looser 😈 </p>", unsafe_allow_html=True)

st.write("Click a button above to play again!")
