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
    """
    Convert input to lower case. 
    """
    return value.lower()

highest_expenses=0

def get_total_and_highest_expenses():
    """ 
    Loops through the numbers in the spreadsheet,
    checks for the highest expense and add all the numbers to get total expenses.
    """
    total_expenses=0

    expenses_dict={}
    all_expenses=expenses.get_all_values()
    if len(all_expenses) > 1:
        for index in range(len(all_expenses)):
            if index > 0:
                total=0
                inner=all_expenses[index]
                for index_a in range(len(inner)):
                    if index_a > 0:
                        total += int(inner[index_a])
                        total_expenses += int(inner[index_a])
                expenses_dict.update({inner[0]:total})
        global highest_expenses  
        highest_expenses = max(expenses_dict, key=expenses_dict.get)
    else:
        total_expenses = "Expenses is currently empty. Enter update to add values.\n"
    print(f'Total Expenses: {total_expenses}\n')

def get_total_income():
    """ 
    Loops through the numbers in the spreadsheet.
    Add all the numbers to get total expenses.
    """
    total_income=0

    all_income=income.get_all_values()
    if len(all_income) > 1:
        for index in range(len(all_income)):
            if index > 0:
                inner=all_income[index]
                for index_a in range(len(inner)):
                    if index_a > 0:
                        total_income += int(inner[index_a])
    else:
        total_income = 'Income is currently empty. Enter "Update" to add values.\n'
    print(f'Total Income: {total_income}\n')



def initialize_app():
    """
    Display messages to guide users on how to use the app. 
    """
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