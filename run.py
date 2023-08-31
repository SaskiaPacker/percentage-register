# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import gspread
from google.oauth2.service_account import Credentials
import itertools

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
    pupil = "pupils"
    print("Please enter the total number of students in the school.\n")
    print(f"For example: 736 {pupil}\n")

    total = int(input("Enter the total here: \n"))
    print("------")
    print("Data is Valid\n")

    return total

def input_year():
    """
    Gets input from the user for the total number of absentees
    per year
    """

    print("Please enter the number of absent students, per year\n")
    print("Starting with year 7 and ending with year 11\n")
    print("For example: 10,20,30,40,50")
    print("------")

    input_data = input("Enter your data here: \n")
    print(f"The data provided is {input_data}")




def main():
    name_input()
    input_data_total()
    input_year()

   
main()
