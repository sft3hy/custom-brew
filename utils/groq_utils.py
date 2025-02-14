from groq import Groq
import newspaper
import os
from config import news_summarizer_system_prompt, SUMMARIZER_MODEL, formatter_system_prompt

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

def extract_news_text(url):
    try:
        article = newspaper.article(url)
        return article.text
    except Exception as e:
        return f"Error extracting article: {e}"


def generate_summary(article_url: str) -> str:
    article = extract_news_text(article_url)
    chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": news_summarizer_system_prompt,
        },
        {
            "role": "user",
            "content": f"summarize this article in an engaging tone: {article}",
        }
    ],
    model=SUMMARIZER_MODEL,
    )
    response = chat_completion.choices[0].message.content
    return response

def format_summaries(llm_output: str) -> str:
    chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": formatter_system_prompt,
        },
        {
            "role": "user",
            "content": f"translate these summaries to html: {llm_output}",
        }
    ],
    model=SUMMARIZER_MODEL,
    )
    response = chat_completion.choices[0].message.content
    return response