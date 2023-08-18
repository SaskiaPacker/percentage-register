# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
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
SHEET = GSPREAD_CLIENT.open('absent_register')


sales = SHEET.worksheet('average_absence_for_week')

data = sales.get_all_values()

def name_input():
    """
    User inputs name and is asked to then input the data 
    """

    name = input("Please Enter your name: ")

    print("------")
    print(f"Welcome {name}\n")



def input_data_total():
    """
    Gets the user to input the total number of students/employees in the whole company
    """
    while True:
        print("Please enter the total number of students in the school.\n")
        print("For example: 736\n")

        total = input("Enter the total here: \n")
        print(total)
        
        if convert_data_values(total):
            print("Data is Valid")
            break
        return total




def input_data_absent():


def convert_data_values():


    

def main():
    """
    Run all program functions
    """
    name_input()
    input_data_total()


main()