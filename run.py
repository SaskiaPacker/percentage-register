# Structure and some code of project taken Love sandwiches 
# Sourced help from a friend who is a developer, who will 
# be credited in my ReadMe file.
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

    return name

    

def input_data_total():
    """
    Gets the user to input the total number of students/employees in the whole company
    """
    
    print("Please enter the total number of students in the school.\n")
    print("For example: 736 pupils\n")

    total = int(input("Enter the total here: \n"))
    print(f"{total} pupils\n")
    print("Data is Valid\n")
    print("------")

    return total



def input_year():
    """
    Gets input from the user for the total number of absentees
    per year
    """
    
    while True:
        print("Please enter the number of absent students, per year\n")
        print("Starting with year 7 and ending with year 11\n")
        print("For example: 10,20,30,40,50")
        print("------")
        
        input_data = input("Enter your data here: \n")
        input_data_list = input_data.split(",")
        
        if data_validation(input_data_list):
            print("Data is Valid!")
            break

    return input_data_list


def data_validation(values):
    """
    gets values from user and changes them to integers,
    checks for only 5 values and will throw back ValueError
    if more than 5 values
    """
    try:
        [int(value) for value in values]
        if len(values) != 5:
            raise ValueError(f"Please enter 5 values, you entered {len(values)}")

    except ValueError as e:
        print(f"Ivalid data: {e}, please try again.\n")
        return False

    return True

def update_data_sheet(list_absences):
    """
    updates the google doc with the input data 
    """

    print("Updating absent per year worksheet...\n")
    input_year_list = SHEET.worksheet("absent_per_year")
    input_year_list.append_row(list_absences)
    print("Absent per year worksheet updated.\n")


def calculate_percentage_absent(total_pupils, list_input):
    """
    calculates input data list and input_data_total 
    and calculates the percentage of the absentees for that week
    """

    list_input = list(map(int, list_input))
    print(list_input)
    total = 0 

    for i in range(0, len(list_input)):
        total = total + list_input[1]

    print("Total absentees is", total)


    


def main():
    name = name_input()
    total_pupils = input_data_total()
    list_absences = input_year()
    update_data_sheet(list_absences)
    calculate_percentage_absent(total_pupils, list_absences)
   
main()
