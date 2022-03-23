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
    Add all the numbers to get total income.
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

def get_all_income():
    """
    clear the terminal, get income from spread sheet
    and display it in a table
    """
    # os.system('cls' if os.name == 'nt' else 'clear')
    all_income = income.get_all_values()
    if all_income:
        table = PrettyTable()
        print('Annual Income Sheet')
        table.field_names=all_income[0]
        for index in range(len(all_income)):
            if index > 0:
                table.add_row(all_income[index])
        print(table)
        get_total_income()
    else:
        print(
          '''
            Income has been cleared. You need to reconstruct the sheet from it's header with "Update"
          ___________________________________\n'''
        )

def get_all_expenses():
     """
    clear the terminal, get expenses from spread sheet
    and display it in a table
    """
    all_expenses = expenses.get_all_values()
    if all_expenses:
        table = PrettyTable()
        print('Annual expenses sheet')
        table.field_names=all_expenses[0]
        for index in range(len(all_expenses)):
            if index > 0:
                table.add_row(all_expenses[index])
        print(table)
        get_total_and_highest_expenses()
    else:
        print(
          '''
          Expenses has been cleared. You need to reconstruct the sheet from it's header with "Update"
          ___________________________________\n
          '''
        )

def update_budget_new(section, data):
    '''
    convert data_array from string to number
    Add new row to budget app
    '''
    print("Updating budget........")
    budget_data = []
    for index in range(len(data)):
        if index != 0:
            budget_data.append(int(data[index]))
        else:
            budget_data.append(data[index])
        
    worksheet = SHEET.worksheet(section)
    print(budget_data)
    worksheet.append_row(budget_data)
    print(
      '''
      Row updated successfully.
      ___________________________\n
      '''
    ) 
    initialize_app()




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