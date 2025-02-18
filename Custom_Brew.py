import streamlit as st
from utils.helpers import validate_email
from utils.email_utils import send_email
from utils.gsheets_utils import update_sheet

st.set_page_config(page_title="Custom Brew", layout="centered", page_icon=":material/newspaper:")

st.title('Custom Brew')
st.write("Welcome to the custom brew! This project compiles news articles tailored to your interests and sends you a daily or weekly newsletter. To get started, please enter your email and topics of interest.")

user_email = st.text_input('Email', placeholder='Enter your email address')
topics = st.radio("Choose a topic", options=["Business", "Entertainment", "General", "Health", "Science", "Sports", "Technology"])
# frequency = st.radio('Email Frequency', options=['Daily', 'Weekly'], index=0)
submit = st.button('Sign me up', type='primary')
valid_email = True

if user_email:
    valid_email = validate_email(user_email)
else:
    valid_email = False

if user_email and topics and submit and valid_email:# and frequency:
    # update the user spreadsheet
    with st.spinner("Adding you to our database..."):
        update_sheet(email=user_email, topic=topics)#  frequency=frequency)
    st.success(f"Welcome to the newsletter! Check your inbox daily at 9am EST for your {topics} Custom Brew ☕")
    welcome_email = open("static/welcome_email.html", "r").read()
    send_email(email_recipient=user_email, body=welcome_email, subject="Welcome to the Custom Brew ☕")


elif submit and not user_email:
    st.error("Please enter your email address.")
elif submit and not topics:
    st.error("Please enter topics of interest.")
elif submit and not topics and not user_email:
    st.error("Please enter both your email address and topics of interest.")
elif submit and not valid_email:
    st.error("Please enter a valid email address.")