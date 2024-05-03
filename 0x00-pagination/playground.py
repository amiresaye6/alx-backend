#!/usr/bin/env python3
"""
pagination
this module is a playground for pythond and it's modules
it will contain my experaments with the new technology i sdudied  for this task
"""
import random
import pandas as pd
from time import sleep

# to calculate the total number of pages
dataset = [random.randint(0, 1000) for _ in range(100)]
total_items = len(dataset)
page_size = 3
total_pages = (total_items + page_size - 1) // page_size

# print(dataset)
# print(total_pages)


# to import data from a .csv file 

# Read the CSV file into a DataFrame
df = pd.read_csv('Popular_Baby_Names.csv')

# Display the first few rows of the DataFrame
# print(df.head(5))

# item_no = input("enter the item idex you want: ")
# print(df[0: int(item_no)])
print(len(df))

new_page_size = 15

pages = (len(df) + new_page_size - 1) // new_page_size
print(pages)

interrrupt = ''
start_index = 0
end_index = new_page_size
while interrrupt == '':
    print(df[start_index:end_index])
    # sleep(2)
    interrrupt = input(
        "type any thing to quite or press enter to contine to next patge")
    start_index = end_index + 1
    end_index += new_page_size
