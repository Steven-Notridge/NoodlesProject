# Initial Creation.

import pandas as pd

data = pd.read_csv("Data/NoodlesData.csv")

userinput = input('rating ')

print(type(userinput))

results = data[data['Rating'].astype('str').str.contains(userinput)]
print(results)