import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
import json
cred = json.loads(os.getenv("GOOGLE_SHEETS_CREDENTIALS"))
# Define the scope of the API access
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

# Authenticate using the service account's JSON file
# creds = ServiceAccountCredentials.from_json_keyfile_name('path/to/your/service-account-file.json', scope)
creds = ServiceAccountCredentials.from_json_keyfile_dict(cred, scope)

def update_sheet(email: str, frequency: str, topic: str):
    client = gspread.authorize(creds)
    sheet = client.open("Custom_brew_users").sheet1
    # Add a new row to the sheet
    row = [email, frequency, topic]  # Data to insert
    sheet.append_row(row)
    print(f"Row added successfully!: {row}")

# update_sheet("email@email.com", "Weekly", "News")