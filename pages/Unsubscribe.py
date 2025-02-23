import streamlit as st
from utils.gsheets_utils import delete_row

st.set_page_config(page_title="Unsubscribe", page_icon=":material/unsubscribe:")

# get parameters from url
params = st.query_params
if 'email' in params and 'topic' in params:
    topic = params['topic']
    email = params['email']
    st.text(f"Howdy {email}, are you sure you wish to unsubscribe from the {topic} Custom Brew?")
    col1, col2, col3 = st.columns([0.4, 0.2, 0.4])
    with col2:
        unsub = st.button('Unsubscribe', type='primary')
    if unsub:
        delete_row(email=email, topic=topic)
        st.success(f"You have successfully unsubscribed, we'll miss you! You'll no longer receive daily {topic.lower()} emails.")
else:
    email = st.text_input("Enter your email:")
    options=["Business", "Entertainment", "General", "Health", "Science", "Sports", "Technology"]
    topic = st.radio(
        "Choose a topic to unsubscribe from:", options,
    )    
    unsub = st.button("Unsubscribe", type='primary')
    if unsub:
        delete_row(email=email, topic=topic)
        st.success(f"You have successfully unsubscribed, we'll miss you! You'll no longer receive daily {topic.lower()} emails.")
