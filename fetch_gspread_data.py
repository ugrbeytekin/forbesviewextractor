import gspread
from oauth2client.service_account import ServiceAccountCredentials
import time
import json

# Path to your downloaded credentials JSON file
SERVICE_ACCOUNT_FILE = 'C:\\Users\\Nemo\\Desktop\\forbexviewexrava\\loyal-gateway-432515-e0-088816095ec1.json'

# Define the scope and credentials
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name(SERVICE_ACCOUNT_FILE, scope)
client = gspread.authorize(creds)

# The ID of your spreadsheet
spreadsheet_id = '1PxIp-ggZ6l1QXLQ9wPCO1nbXA2ZUb9nRzzzGOtOJ0Ks'

# Retry logic to handle potential transient errors
MAX_RETRIES = 5
RETRY_DELAY = 30  # Increase delay to 30 seconds
FETCH_INTERVAL = 300  # Time to wait between fetches, in seconds (300s = 5 minutes)

def fetch_data():
    for attempt in range(MAX_RETRIES):
        try:
            # Open the spreadsheet by ID and get the data from the specified range
            spreadsheet = client.open_by_key(spreadsheet_id)
            worksheet = spreadsheet.sheet1  # Assuming you want the first sheet
            data = worksheet.get('F:I')  # Get data from columns F to I

            # Convert the data to a list of dictionaries
            headers = ["Title1", "View Count1", "Date Published1", "Title_URL1"]
            json_data = [dict(zip(headers, row)) for row in data]

            # Write the data to a JSON file
            with open('forbes_blog_data.json', 'w') as json_file:
                json.dump(json_data, json_file, indent=2)
            
            return json_data  # If successful, return the data
        except gspread.exceptions.APIError as e:
            print(f"Attempt {attempt + 1} failed with error: {e}")
            if attempt < MAX_RETRIES - 1:
                time.sleep(RETRY_DELAY)
            else:
                raise  # If all retries fail, raise the exception

# Main loop to fetch data at regular intervals
while True:
    try:
        data = fetch_data()
        print("Fetched data and saved to JSON:")
        for row in data:
            print(row)
    except Exception as e:
        print(f"Failed to fetch data: {e}")
    
    # Wait for the next interval
    time.sleep(FETCH_INTERVAL)
