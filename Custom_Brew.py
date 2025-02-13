import streamlit as st
from utils.helpers import validate_email
from utils.news_utils import get_news

st.set_page_config(page_title="Custom Brew", layout="centered", page_icon=":material/newspaper:")

st.title('Custom Brew')
st.write("Welcome to the custom brew! This project compiles news articles tailored to your interests and sends you a daily or weekly newsletter. To get started, please enter your email and topics of interest.")

user_email = st.text_input('Email', placeholder='Enter your email address')
topics = st.text_input('Topics', placeholder='Enter topics separated by commas')
frequency = st.radio('Email Frequency', options=['Daily', 'Weekly'], index=1)
submit = st.button('Create my brew', type='primary')
valid_email = True

if user_email:
    valid_email = validate_email(user_email)
else:
    valid_email = False

if user_email and topics and submit and valid_email and frequency:
    # Process the input and send the newsletter
    get_news(topics)

elif submit and not user_email:
    st.error("Please enter your email address.")
elif submit and not topics:
    st.error("Please enter topics of interest.")
elif submit and not topics and not user_email:
    st.error("Please enter both your email address and topics of interest.")
elif submit and not valid_email:
    st.error("Please enter a valid email address.")