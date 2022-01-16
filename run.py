import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('budget_app')

def get_income_data():
    """ 
    Get income figures input from the user
    """
    print("Welcome to the budget app.")
    
    data_str = input("Please enter the value of your income here: \n")
    print(f"The data provided is {data_str}")

get_income_data()