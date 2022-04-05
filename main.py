# Initial Creation.

import pandas as pd

# Grab the data we need from the csv
data = pd.read_csv("Data/NoodlesData.csv")
pd.set_option('display.max_colwidth', None)
pd.set_option('display.max_columns', None)

# Creating the Menu Options that will be displayed to EndUser
menu_options = {
    1: 'Rating',
    2: 'Option 2',
    3: 'Option 3',
    4: 'Exit',
}


# Function to enable Error checking when prompting the user for a Number. The only numbers we're going to allow really are between 1 and 5.
def get_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Sorry, this requires a number between 1 and 5.")
            continue
        if value < 0:
            print("It can't be a negative.")
            continue
        elif value > 5:
            print("Your number cannot be more than 5.")
            continue
        else:
            break
    return value


def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )


def option1():
    # Request Users input
    # userinput = input('What Rating would you like to search for: ')
    userinput = get_integer_input("What Rating would you like to search for: ")
    # Because we are using a Function to enable Errors for the inputs, we need to convert the integer into a String, to avoid more errors!
    str_userinput = str(userinput)
    # Retrieve the Data from the csv based on the input from user. We also convert the integer input as a String, because accessor doesn't like them.
    results = data[data['Rating'].astype('str').str.contains(str_userinput)]
    # Create a new DataFrame with the Headings we wish to display, along with where the information is retrieved from.
    # We have to use data=results because we want the Data to be specific to what the User is looking for.
    df = pd.DataFrame(columns=['Name (Brand)', 'Accuracy', 'Rating', 'Artificial', 'Broth', 'Price', 'Flavour', 'Seasoning', 'Key1', 'Key2', 'Key3'], data=results)
    # Formatting is for winners.
    df.style.set_properties(subset=['Name (Brand)'], **{'text-align': 'left', 'width': '300px'})
    df.sort_values('Rating')
    # Print the Results.
    print(df)


# Running the code together.
if __name__=='__main__':
    while(True):
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number ...')
        # Check what choice was entered and act accordingly
        if option == 1:
            option1()
        elif option == 2:
            option2()
        elif option == 3:
            option3()
        elif option == 4:
            print('Thanks message before exiting')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 4.')