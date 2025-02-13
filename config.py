import os

NEWS_API_KEY = os.getenv("NEWS_API_KEY")

sample_news_summary = """
Teacher Marc Fogel back in US after prisoner swap with Russia. The call between Trump and
Putin came after Fogel, an American arrested for flying into Moscow with medically prescribed 
marijuana in 2021, returned to US soil as part of a prisoner exchange. To secure Fogel's freedom,
the Trump administration agreed to releaseAlexander Vinnik, a Russian citizen and the 
co-founder of Bitcoin exchange BTC-e, which US authorities say was used by criminals 
for ransomware schemes, identity theft, and drug trafficking. Vinnik, who pleaded guilty
to conspiracy to commit money laundering, will leave $100 million worth of digital assets 
in the US as part of the deal, per NBC.
"""

news_summarizer_system_prompt = """
You are a news summarization system that takes in a news summary and returns a summary.
The summary should include key points from the original news article. Please title the summary.
"""

