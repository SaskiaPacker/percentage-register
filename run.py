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


def input_data_absent():
    """
    Gets the user to input the data and adds all of the numbers together
    to get a total number of absent pupils, per year
    """

    print("Please enter the amount of absent pupils per year\n")
    print("starting with year 7 and ending with year 11\n")

    year_group = "year 7"
    print(f"For example: {year_group}: 12 absent\n")

    data_input = ''
    while True:

        data_input = input("Enter your values in here. Enter done to finish\n")
        data_list = data_input.split(",")

        year_values = ["year 7", "year 8", "year 9", "year 10", "year 11"]
        for x in year_values:    
            print(x + " " + "absent:") 
            print(data_list)
        print("Data is valid")

        break 

            
            

# a,b,c,d,e = input("Enter your values\n ").split()
# print(" Year 7: {} absent, Year 8: {} absent, Year 9: {} absent, Year 10: {} absent, Year 11: {} absent".format(a,b,c,d,e))
# print()


def main():
    name_input()
    input_data_total()
    input_data_absent()


main()
