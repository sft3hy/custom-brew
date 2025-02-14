import schedule
import time
import json
import threading
from utils.email_utils import send_email
from utils.groq_utils import generate_summary, format_summaries
from utils.news_utils import get_news
from dummy_news_response import dummy
from config import EMAIL_SEND_TIME, TIME_BETWEEN_JOB_CHECK
import subprocess

# Function to send emails (Placeholder)
def send_email_scheduler(email, topics):
    print(f"Generating email for {email} about {topics}")
    # news_info = get_news(topic=topics)
    news_info = dummy
    summaries = ""
    for article in news_info:
        summaries += generate_summary(article['url']) + '<br>'
        summaries += f'<a href="{article["url"]}" target="_blank">{article["title"]}</a><br><br><br>'
    with open("current_output.html", "w") as file:
        file.write(summaries)
    send_email(subject="Custom Brew", body=f"<!DOCTYPE html><html><body>{format_summaries(summaries).replace("**", "")}</body></html>", email_recipient=email)

# Function to schedule Daily email jobs
def schedule_daily_emails():
    for job in json.load(open('jobs.json'))["Daily"]:
        schedule.every().day.at(EMAIL_SEND_TIME).do(send_email_scheduler, job["email"], job["topics"])

# Function to schedule weekly email jobs
def schedule_weekly_emails():
    for job in json.load(open('jobs.json'))["Weekly"]:
        schedule.every().sunday.at(EMAIL_SEND_TIME).do(send_email_scheduler, job["email"], job["topics"])

# Function to reload schedule when jobs change
def update_schedule():
    schedule.clear()
    schedule_daily_emails()
    schedule_weekly_emails()

# Function to add a new job (called from Streamlit)
def add_email_job(frequency, email, topics):
    if frequency == "Daily":
        json.load(open('jobs.json'))["Daily"].append({"email": email, "topics": topics})
    elif frequency == "Weekly":
        json.load(open('jobs.json'))["Weekly"].append({"email": email, "topics": topics})

    with open("jobs.json", "r") as file:
        old_json = json.load(file)
    file.close()
    job_info = {
        "email": email,
        "topics": topics,
    }

    # Append the job to the correct category
    if frequency == "Daily":
        old_json["Daily"].append(job_info)
    elif frequency == "Weekly":
        old_json["Weekly"].append(job_info)

    # Save updated jobs back to jobs.json
    print("Added email jobs to jobs.json")
    with open("jobs.json", "w") as file:
        json.dump(old_json, file, indent=4)
    file.close()
    update_schedule()

# Background scheduler loop
def run_scheduler():
    while True:
        print("Checking scheduled jobs...")
        schedule.run_pending()
        time.sleep(TIME_BETWEEN_JOB_CHECK)

# Run the scheduler
def run_scheduler():
    update_schedule()  # Ensure schedule loads initially
    while True:
        print("Checking scheduled jobs...")
        schedule.run_pending()
        time.sleep(TIME_BETWEEN_JOB_CHECK)


if __name__ == "__main__":
    print("Starting job runner...")
    run_scheduler()


# Example of adding a new email job (this would be done via your Streamlit app)
# add_email_job("Daily", "newuser@example.com", "technology")
