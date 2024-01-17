print("Hello World!")

num1 = int(input("Enter an integer: "))
num2 = int(input("Enter another integer: "))
print("The sum of the two numbers is:", num1 +num2)

fruits = []
for i in range(1,6):
    fruits.append(input(f"Name of Fruit {i}: "))
print(fruits)

import pandas as pd
forest = pd.read_csv("/anvil/projects/tdm/data/forest/ENTIRE_COUNTY.csv")
forest.info
forest.info()
forest.shape
forest.size
forest.columns
len(forest)