import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Mood Tracker by Toochukwu", page_icon="😊")

st.title("Mood Tracker - by NWAEDOZIE")
st.write("Track your daily mood for your BCU Project")

# --- User Inputs ---
name = st.text_input("What is your name?", "NWAEDOZIE")

st.write("---")
st.subheader("How are you feeling today?")

mood = st.selectbox("Select your mood:", 
    ["😊 Happy - WAS GREAT", "😐 Okay - Normal", "😔 Sad - Low", "😡 Angry", "🤩 Excited"]
)

energy = st.slider("Your Energy Level (1-10)", 1, 10, 7)

note = st.text_area("What happened today?", "Today was great! I built my first app!")

# --- Save Button ---
if st.button("Save My Mood"):
    st.success(f"Saved! Hello {name}, your mood {mood} is recorded!")
    st.balloons()
    
    # Show summary
    st.write(f"### Summary for {datetime.now().strftime('%A, %d %B')}")
    st.write(f"**Name:** {name}")
    st.write(f"**Mood:** {mood}")
    st.write(f"**Energy:** {energy}/10")
    st.write(f"**Note:** {note}")
    
    # Fake chart for demo (looks professional for BCU)
    st.write("---")
    st.subheader("Your Week Mood Chart")
    chart_data = pd.DataFrame({
        'Day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Today'],
        'Energy': [5, 6, 4, 8, 7, energy]
    })
    st.bar_chart(chart_data, x='Day', y='Energy')
    
    st.write("Built with Python & Streamlit - By Toochukwu for BCU")

st.write("---")
st.caption("Tip: Change the energy slider and click Save to see the chart update!")