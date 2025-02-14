import os

NEWS_API_KEY = os.getenv("NEWS_API_KEY")

sample_news_summary = """
Teacher Marc Fogel back in US after prisoner swap with Russia. The call between Trump and
Putin came after Fogel, an American arrested for flying into Moscow with medically prescribed 
marijuana in 2021, returned to US soil as part of a prisoner exchange. To secure Fogel's freedom,
the Trump administration agreed to release Alexander Vinnik, a Russian citizen and the 
co-founder of Bitcoin exchange BTC-e, which US authorities say was used by criminals 
for ransomware schemes, identity theft, and drug trafficking. Vinnik, who pleaded guilty
to conspiracy to commit money laundering, will leave $100 million worth of digital assets 
in the US as part of the deal, per NBC.
"""

news_summarizer_system_prompt = f"""
You are a news summarization system that takes in a news summary and returns a summary.
The summary should include key points from the original news article. Please title the summary and output
your results in pretty HTML format for the purpose of displaying in an email.
This is an example summary for inspiration: {sample_news_summary}
"""

formatter_system_prompt = """
You are a translator. You will be given an llm output, and your job is to translate it into pretty html for the 
purpose of emailing. Do not change any text, just change the formatting for raw html. Add style with your own custom 
css for bold fonts and headers. Output only the html and css. Your output should be able to display in an email.
For example, instead of **bold text** you would write <strong>bold text</strong>. 
"""


EMAIL_SEND_TIME="19:26"
SUMMARY_COUNT=2
SUMMARIZER_MODEL="llama-3.2-1b-preview"
TIME_BETWEEN_JOB_CHECK=10