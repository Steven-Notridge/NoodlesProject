# This file was created, because I was getting tired of constantly typing in the values and navigating the menu...
# It'll likely stay in the project folder, but I will not be adding comments regarding the changes within this.

import pandas as pd

# Grab the data we need from the csv
data = pd.read_csv('Data/NoodlesData.csv')
pd.set_option('display.max_colwidth', None)
pd.set_option('display.max_columns', None)


# To avoid a long line of gibberish, I'm creating a few variable here to make the code easier to read.
revColumns = ['Name (Brand)', 'Accuracy', 'Rating', 'Artificial', 'Broth', 'Price', 'Flavour', 'Seasoning', 'Key1', 'Key2', 'Key3']


# Request Users input
userinput = input('name')
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
