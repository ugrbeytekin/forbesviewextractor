import os
import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Use the secret from GitHub Actions
SERVICE_ACCOUNT_INFO = json.loads(os.getenv('GCP_SERVICE_ACCOUNT'))

# Define the scope and credentials
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_dict(SERVICE_ACCOUNT_INFO, scope)
client = gspread.authorize(creds)

# The ID of your spreadsheet
spreadsheet_id = '1PxIp-ggZ6l1QXLQ9wPCO1nbXA2ZUb9nRzzzGOtOJ0Ks'

# Fetch data from Google Sheets
worksheet = client.open_by_key(spreadsheet_id).sheet1
data = worksheet.get_all_records()

# Convert the fetched data to JSON format
json_data = data  # Assuming 'data' is the list of dictionaries fetched from the sheet

# Debugging: Print the current working directory
print("Current working directory:", os.getcwd())

# Write the JSON file in the current directory
json_file_path = os.path.join(os.getcwd(), 'forbes_blog_data.json')

with open(json_file_path, 'w') as json_file:
    json.dump(json_data, json_file, indent=2)

print(f"JSON data saved to {json_file_path}")
