# Created by Steven Notridge, https://github.com/steven-notridge
# v0.1;
# Added Broth and Name searching, also added Error checking for the Name search.
# I may need to make a new method for searching strings, because I want to be able to search by string on flavour and tags.

import pandas as pd

# Grab the data we need from the csv
data = pd.read_csv("Data/NoodlesData.csv")
pd.set_option('display.max_colwidth', None)
pd.set_option('display.max_columns', None)

# Creating the Menu Options that will be displayed to EndUser
menu_options = {
    1: 'Rating',
    2: 'Broth',
    3: 'Name (Brand)',
    4: 'Exit',
}


# To avoid a long line of gibberish, I'm creating a few variable here to make the code easier to read.
revColumns = ['Name (Brand)', 'Accuracy', 'Rating', 'Artificial', 'Broth', 'Price', 'Flavour', 'Seasoning', 'Key1', 'Key2', 'Key3']


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


# Another function for str values instead of int.
# def get_string_input(prompt, input_type=str):
# This will likely go unused now I've figured out the Dataframe if statement, but I'll keep this just in case it has some use in the future as it works.
def get_string_input(prompt):
    while True:
        try:
            value = input(prompt)
            # return input_type (input(prompt))
        except ValueError:
            print("It broke!")
            continue
        else:
            break
    return value


def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )


def opt_rating():
    # Request Users input
    userinput = get_integer_input("What Rating would you like to search for: ")
    # Because we are using a Function to enable Errors for the inputs, we need to convert the integer into a String, to avoid more errors!
    str_userinput = str(userinput)
    # Retrieve the Data from the csv based on the input from user. We also convert the integer input as a String, because accessor doesn't like them.
    results = data[data['Rating'].astype('str').str.contains(str_userinput)]
    # Create a new DataFrame with the Headings we wish to display, along with where the information is retrieved from.
    # We have to use data=results because we want the Data to be specific to what the User is looking for.
    df = pd.DataFrame(columns=revColumns, data=results)
    # Formatting is for winners.
    # Ensuring the Brand stays if it goes to a new line etc.
    df = df.set_index(['Name (Brand)'])
    # Aligning the text within the Name column to the left and ensuring there is no cutoff.
    df.style.set_properties(subset=['Name (Brand)'], **{'text-align': 'left', 'width': '300px'})
    # Sorting by Rating by Descending.
    df.sort_values('Rating')
    # Print the Results.
    print(df)


def opt_broth():
    # Basically identical to the opt_rating, check there for notes.
    userinput = get_string_input("What score of Broth would you like to search for: ")
    str_userinput = str(userinput)
    results = data[data['Broth'].astype('str').str.contains(str_userinput)]
    df = pd.DataFrame(columns=revColumns, data=results)
    df = df.set_index(['Name (Brand)'])
    df.style.set_properties(subset=['Name (Brand)'], **{'text-align': 'left', 'width': '300px'})
    df.sort_values('Broth')
    print(df)


def opt_name():
    userinput = input('What is the name of the Brand you wish to search for: ')
    # Retrieve the Data from the csv based on the input from user. We also convert the integer input as a String, because accessor doesn't like them.
    # Create a new DataFrame with the Headings we wish to display, along with where the information is retrieved from.
    # In this case, we just reference the original data instead of the results like in Rating, because although it would work, we cannot do any error checking.
    df = pd.DataFrame(columns=revColumns, data=data)
    # Formatting is for winners.
    df = df.set_index(['Name (Brand)'])
    df.style.set_properties(subset=['Name (Brand)'], **{'text-align': 'left', 'width': '300px'})
    df.sort_values('Rating')
    # Now we need to check if the users input is actually in the Name column, which will proceed to the next line.
    if userinput in df.index:
        # If userinput is located, we now print the results, whilst also filtering them to match the name of the input.
        print(df[df.index.str.contains(userinput)])
    # If we cannot locate userinput within the Name column, we proceed with the below.
    else:
        print("There doesn't seem to be a name or brand that matches your input.")


# Running the code together.
if __name__=='__main__':
    while True:
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number ...')
        # Check what choice was entered and act accordingly
        if option == 1:
            opt_rating()
        elif option == 2:
            opt_broth()
        elif option == 3:
            opt_name()
        elif option == 4:
            print('Exiting...')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 4.')