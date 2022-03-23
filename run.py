import os
import gspread
from google.oauth2.service_account import Credentials
from prettytable import PrettyTable
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('budget_app')

income = SHEET.worksheet('income')
expenses = SHEET.worksheet('expenses')

def check_input_type(text):
    '''Checks if the user enters an alphabet or a number.
       Returns an error message if the user enters a number.
    '''
    if text.isnumeric():
        # os.system('cls' if os.name == 'nt' else 'clear')
        print('Invalid input. Please enter alphabets')
    else:
        return True

def convert_to_lowercase(value):
    # Convert input to lower case. 
    return value.lower()



def initialize_app():
    initialize = True
    while initialize:
        print('Welcome to the Budget App!\n')
        print('Please enter "All" to display all recorded income and expenses.\n')
        print('Please enter "Income" to display all recorded income.\n')
        print('Please enter "Expenses" to display all recorded expenses.\n')
        print('Please enter "Update" to make changes to the budget.\n')
        print('Please enter "Highest" to get the your highest expenses.\n')
        print('Enter "clear" to clear worksheet.\n')
        print('To end the process please enter "Exit".\n')
      
        user_input = input('Enter your data here: ')
        'Validate input type'

        if check_input_type(user_input) == True:
            check_entered_values(convert_to_lowercase(user_input))


initialize_app()