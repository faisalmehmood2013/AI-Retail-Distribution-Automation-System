from flask import Flask, render_template
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Initialize the Flask application
app = Flask(__name__)

# # --- Google Sheets Configuration ---

# # NOTE: Replace 'path/to/your/service_account.json' with the actual path 
# # to the JSON key file you downloaded from Google Cloud.
# SERVICE_ACCOUNT_FILE = 'credential.json' 
# # NOTE: Replace 'Your Live Inventory Sheet Name' with the exact name of your Google Sheet.
# SHEET_NAME = 'Stock Register' 
# # Define API access scope for reading sheets
# SCOPE = [
#     'https://www.googleapis.com/auth/spreadsheets.readonly',
#     'https://www.googleapis.com/auth/drive.readonly'
# ]

# # --- Authentication ---
# try:
#     # Authorize the service account credentials
#     CREDS = ServiceAccountCredentials.from_json_keyfile_name(SERVICE_ACCOUNT_FILE, SCOPE)
#     CLIENT = gspread.authorize(CREDS)
# except Exception as e:
#     # Handle critical authentication errors during startup
#     print(f"CRITICAL ERROR: Failed to authorize Google Sheets API. Check your JSON file path and credentials. Error: {e}")
#     CLIENT = None # Set client to None if auth fails

# --- Routes ---

# 1. Home Page Route
@app.route('/')
def index():
    # Render the index.html template
    return render_template('index.html')

# 2. Inventory Tab Route (Fetches Live Data)
# @app.route('/inventory') 
# def inventory_data():
#     """Fetches live inventory data from Google Sheet and renders the inventory.html template."""
#     if CLIENT is None:
#         return "ERROR: Google Sheets connection failed at startup.", 500
    
    # try:
    #     # Open the spreadsheet by its name
    #     spreadsheet = CLIENT.open('Nestle Water Distribution')
    #     # Select the specific worksheet (assuming 'sheet1' is where data is)
    #     worksheet = spreadsheet.sheet1 
        
    #     # Fetch all data as a list of dictionaries (records)
    #     data = worksheet.get_all_records() 
        
    #     # Render the 'inventory.html' template and pass the data
    #     return render_template('inventory.html', sheet_data=data)
        
    # except gspread.exceptions.SpreadsheetNotFound:
    #     return f"ERROR: Spreadsheet '{'Stock Register'}' not found. Check the sheet name and sharing permissions.", 404
    # except Exception as e:
    #     # Handle any other exceptions during data fetching
    #     print(f"Error fetching inventory data: {e}")
    #     return "Sorry, we could not fetch the inventory data right now due to an unexpected error.", 500

# Run the app
if __name__ == '__main__':
    # Run the app in debug mode
    app.run(debug=True)