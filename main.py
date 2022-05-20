# Created by Steven Notridge, https://github.com/steven-notridge
# v0.3;
# Changed the Width of the DataFrames again, now it extends the entire Terminal. Not sure who I didn't try this one before.
# Overall Score and Price Per Point has been added.

import pandas as pd

# Grab the data we need from the csv
data = pd.read_csv("Data/NoodlesData.csv")
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
pd.options.display.float_format = '{:.3f}'.format

# Creating the Menu Options that will be displayed to EndUser
menu_options = {
    1: 'Rating',
    2: 'Broth',
    3: 'Name (Brand)',
    4: 'Flavour',
    5: 'Exit',
}

# To avoid a long line of gibberish, I'm creating a few variable here to make the code easier to read.
revColumns = ['Name (Brand)', 'Accuracy', 'Rating', 'Artificial', 'Broth', 'Price', 'Flavour', 'Seasoning', 'Key1',
              'Key2', 'Key3']


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
        print(key, '--', menu_options[key])


def opt_rating():
    print("\n")
    # Request Users input
    userinput = get_integer_input("What Rating would you like to search for: ")
    # Because we are using a Function to enable Errors for the inputs, we need to convert the integer into a String, to avoid more errors!
    str_userinput = str(userinput)
    # Retrieve the Data from the csv based on the input from user.
    results = data[data['Rating'].astype('str').str.contains(str_userinput)]
    # Create a new DataFrame with the Headings we wish to display, along with where the information is retrieved from.
    # We have to use data=results because we want the Data to be specific to what the User is looking for.
    df = pd.DataFrame(columns=revColumns, data=results)
    # Formatting is for winners.
    # Ensuring the Brand stays if it goes to a new line etc.
    df = df.set_index(['Name (Brand)'])
    # Aligning the text within the Name column to the left and ensuring there is no cutoff.
    df.style.set_properties(subset=['Name (Brand)'], **{'text-align': 'left'})
    # Sorting by Rating by Descending.
    df.sort_values('Rating')
    # Adding the Overall Score together.
    df = df.assign(Overall=lambda x: x.Rating + x.Accuracy + x.Broth - x.Artificial)
    # For PPP we need to fix the Price column, because it has the currency symbol. Lambda doesn't work with them and throws an error.
    df['Price'] = df['Price'].str.replace('£', '')
    # Formatting as a Float, using an int was throwing errors.
    df['Price'] = df['Price'].astype(float)
    # Add the PPP column to the end of the table.
    df = df.assign(PricePerPoint=lambda y: y.Price / y.Overall)
    # Change the decimals of PPP to 2.
    # df.style.format({
    #     'PricePerPoint': '{:,.2f}%'.format,
    # })
    # Print the Results.
    print(df)
    print("\n")


def opt_broth():
    print("\n")
    # Basically identical to the opt_rating, check there for notes.
    userinput = get_integer_input("What score of Broth would you like to search for: ")
    str_userinput = str(userinput)
    results = data[data['Broth'].astype('str').str.contains(str_userinput)]
    df = pd.DataFrame(columns=revColumns, data=results)
    df = df.set_index(['Name (Brand)'])
    df.style.set_properties(subset=['Name (Brand)'], **{'text-align': 'left'})
    df = df.assign(Overall=lambda x: x.Rating + x.Accuracy + x.Broth - x.Artificial)
    df['Price'] = df['Price'].str.replace('£', '')
    df['Price'] = df['Price'].astype(float)
    df = df.assign(PricePerPoint=lambda y: y.Price / y.Overall)
    df.sort_values('Broth')
    print(df)
    print("\n")


def opt_name():
    print("\n")
    userinput = input('What is the name of the Brand you wish to search for: ')
    # In this case, we just reference the original data instead of the results like in Rating, because although it would work, we cannot do any error checking.
    df = pd.DataFrame(columns=revColumns, data=data)
    # Formatting is for winners.
    df.style.set_properties(subset=['Name (Brand)'], **{'text-align': 'left'})
    df = df.assign(Overall=lambda x: x.Rating + x.Accuracy + x.Broth - x.Artificial)
    df['Price'] = df['Price'].str.replace('£', '')
    df['Price'] = df['Price'].astype(float)
    df = df.assign(PricePerPoint=lambda y: y.Price / y.Overall)
    df.sort_values('Rating')
    # Now we need to check if the users input is actually in the Name column. nameCheck will request a True/False answer.
    nameCheck = df['Name (Brand)'].str.contains(userinput, case=False).any()
    # We'll also check to see if the users input is part of any of the brands.
    nameSearch = df[df['Name (Brand)'].str.contains(userinput, case=False)]
    # If the name IS part of the brands, we use the IF statement to check for TRUE and then continue.
    if nameCheck:
        # If userinput is located, we now print the results, whilst also filtering them to match the name of the input.
        print("\n")
        # We also set the index back to the Name, to make it visible all the time. Doing this before on the df variable caused issues
        # I believe that's due to it breaking the str.contains part, and making it act weird. We don't need to format the data before we use it anyway.
        nameSearch = nameSearch.set_index(['Name (Brand)'])
        print(nameSearch)
        print("\n")
    # If we cannot locate userinput within the Name column, we proceed with the below.
    else:
        print("\n")
        print("There doesn't seem to be a name or brand that matches your input.")
        nameCheck = input("Would you like to get a list of all the Brands that have been reviewed? ")
        if nameCheck in ('yes', 'y', 'Yes', 'Y'):
            print("\n")
            # Creating another DataFrame because we don't want to use one that's already been manipulated.
            namelist = pd.DataFrame(data)
            # Converting the DataFrame to a list, and filtering it based on the str used.
            namelist_filtered = namelist['Name (Brand)'].tolist()
            # A for statement to print out each Name that's included, and to make it look neater for the EndUser as a string rather than a list.
            for name in namelist_filtered:
                print(name)
        # If anything else is typed instead of the typical yes formats, execute the below.
        else:
            print("\n")
            print('Okay, going back to menu.')


def opt_flavour():
    userinput = input('What is the Flavour you wish to search for: ')
    df = pd.DataFrame(columns=revColumns, data=data)
    df = df.set_index(['Name (Brand)'])
    df.style.set_properties(subset=['Name (Brand)'], **{'text-align': 'left'})
    df = df.assign(Overall=lambda x: x.Rating + x.Accuracy + x.Broth - x.Artificial)
    df['Price'] = df['Price'].str.replace('£', '')
    df['Price'] = df['Price'].astype(float)
    df = df.assign(PricePerPoint=lambda y: y.Price / y.Overall)
    df.sort_values('Rating')
    flavCheck = df['Flavour'].str.contains(userinput, case=False).any()
    flavSearch = df[df['Flavour'].str.contains(userinput, case=False)]

    if flavCheck:
        print("\n")
        print(flavSearch)
        print("\n")

    # The below is replicated from opt_name - Check the notes there.
    else:
        print("\n")
        print("There doesn't seem to be a flavour that matched your input.")
        nameCheck = input("Would you like to get a list of all the Flavours that have been reviewed? ")
        if nameCheck in ('yes', 'y', 'Yes', 'Y'):
            print("\n")
            nameList = pd.DataFrame(data)
            nameList_filtered = nameList['Flavour'].tolist()
            for name in nameList_filtered:
                print(name)
        else:
            print("\n")
            print('Okay, going back to menu.')


# Running the code together.
if __name__ == '__main__':
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
            opt_flavour()
        elif option == 5:
            print('Exiting...')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 5.')
