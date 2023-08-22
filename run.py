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
    pupil = "pupils"
    print("Please enter the total number of students in the school.\n")
    print(f"For example: 736 {pupil}\n")

    total = int(input("Enter the total here: \n"))
    print("Data is Valid\n")

    return total


def input_data_absent(addition):
    """
    Gets the user to input the data and adds all of the numbers together
    to get a total number of absent pupils
    """

    print("Please enter the amount of absent pupils per year\n")
    print("starting with year 7 and ending with year 11\n")

    year_group = "year 7"
    print(f"For example: {year_group}: 12 absent\n")

    data_input = ''
    while True:
        year_values = 7, 8, 9, 10, 11
        for x in range(7,12):  
            data_input = input("Enter your values in here.\n").split()
            y = ''.join(data_input)
            z = int(y)
            print("year " + str(x)+ " absent:")
            print(z)
        print("Data is valid")
        data_addition = len(z)
        print(data_addition)

        break 

def data_addition():
    """
    Adds up the input data and displays the total
    """
    data_input = ''
    print("Calculating total number of students absent")
    final_sum = len(z)
    print(final_sum)


    


def main():
    name_input()
    input_data_total()
    input_data_absent()
    addition = data_addition()


main()