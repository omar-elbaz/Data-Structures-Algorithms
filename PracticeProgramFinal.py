# # December 8th
# sample_list = [235, 43, 56, 78, 930, 15, 3, 17, 167, 204]

# def LargerThan (a,n):
#     larger_than_n_list = []
#     print()
#     print("The following numbers are greater than n: ")
    
#     for element in a:
#         if element > n:
#             larger_than_n_list.append(element)
#     print(larger_than_n_list)

# LargerThan(sample_list, 100)


import pandas as pd

file_name = input()

# Read the Excel file into a DataFrame
df = pd.read_excel(file_name)

# Print the DataFrame to display the data
print(df)