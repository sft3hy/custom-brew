import streamlit as st
from utils.helpers import validate_email
from scheduler import add_email_job
import subprocess

def start_scheduler():
    try:
        subprocess.Popen(["python", "scheduler.py"])
        st.session_state["scheduler_started"] = True
        print("Scheduler started.")
    except Exception as e:
        print(f"Error starting scheduler: {e}")
# Call the function when the app starts
if "scheduler_started" not in st.session_state:
    start_scheduler()

st.set_page_config(page_title="Custom Brew", layout="centered", page_icon=":material/newspaper:")

st.title('Custom Brew')
st.write("Welcome to the custom brew! This project compiles news articles tailored to your interests and sends you a daily or weekly newsletter. To get started, please enter your email and topics of interest.")

user_email = st.text_input('Email', placeholder='Enter your email address')
topics = st.radio("Choose a topic", options=["Business", "Entertainment", "General", "Health", "Science", "Sports", "Technology"])
frequency = st.radio('Email Frequency', options=['Daily', 'Weekly'], index=1)
submit = st.button('Create my brew', type='primary')
valid_email = True

if user_email:
    valid_email = validate_email(user_email)
else:
    valid_email = False

if user_email and topics and submit and valid_email and frequency:
    # Process the input and send the newsletter
    add_email_job(frequency=frequency, email=user_email, topics=topics)
    st.success(f"Your custom brew has been created! You will receive a {frequency} email at {user_email} about {topics}.")


elif submit and not user_email:
    st.error("Please enter your email address.")
elif submit and not topics:
    st.error("Please enter topics of interest.")
elif submit and not topics and not user_email:
    st.error("Please enter both your email address and topics of interest.")
elif submit and not valid_email:
    st.error("Please enter a valid email address.")