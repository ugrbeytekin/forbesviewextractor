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

# Your existing data fetching code here...
