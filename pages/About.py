import streamlit as st
st.markdown("""
Custom Brew is a personalized newsletter that delivers curated content tailored to your interests and preferences.
## Key Features

* Receive daily or weekly updates on topics of your choice, handpicked by LLMs.
* Get the latest insights and analysis from sources in your favorite fields.
* Customize your experience with your favorite topics and get a daily email with the latest news.

            
## Backend Workflow
            
* The app uses NewsAPI every day to fetch the latest headlines and articles.
* The first LLM gets a list of headlines and chooses what is the most relevant and informative.
* The second LLM gets the article content of each curated relevant headline and article, and generates an informative summary of the article.
* This process runs once a day and emails all subscribers the curated summaries in their selected topic.
            
## About the developer
            
Hey! I'm Sam and I like to make hobby projects like this. Check out my [personal website](https://sft3hy.github.io/sam-townsend). If you have any questions or need help, feel free to email me - smaueltown@gmail.com
""")
