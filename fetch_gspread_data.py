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

# Your data fetching code here...

# Debugging: Print the current working directory
print("Current working directory:", os.getcwd())

# Write the JSON file in the current directory
json_file_path = os.path.join(os.getcwd(), 'forbes_blog_data.json')

# Assuming json_data is the data you want to write
with open(json_file_path, 'w') as json_file:
    json.dump(json_data, json_file, indent=2)

print(f"JSON data saved to {json_file_path}")
