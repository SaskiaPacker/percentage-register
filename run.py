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
    print("Data is Valid\n")

    return total


def input_data_absent():
    """
    Gets the user to input the data and converts all the data to integeres
    """

    print("Please enter the amount of absent pupils per year\n")
    print("starting with year 7 and ending with year 11\n")

    year_group = "year 7"
    print(f"For example: {year_group}: 12 absent\n")

    input_list = []
    while True:
        year_values = 7, 8, 9, 10, 11
        for x in range(7,12):  
            data_input = input("Enter your values in here. Type q to quit\n")
            input_list.extend(data_input)
            print("year " + str(x) + " absent:")
            print(data_input)
            #print(input_list)

        #if data_error_input(input_list):
            #print("Data is valid")
        
        break 
    #print("Data is valid!")
    total_data_list = input_list
    data_error_input(total_data_list)


def data_error_input(values):
    """
    inside the try statement checks if integers inside the list are integers
    """
    print(values)

    try:
        [int(value) for value in values]
        if all(isinstance(values, int) for num in values):
            print("Yes elements are list")
            
        else:
            print("try again")

    except ValueError as e:
        print(e)





def main():
    name_input()
    input_data_total()
    input_data_absent()

main()
