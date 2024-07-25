import pandas as pd
import numpy as np
import os

# Step 1: Ask for File Name
file_name = input("Enter the file name (e.g., 'Montlhly Copy.xls'): ")
file_path = os.path.join(os.path.expanduser('~'), 'Downloads', file_name)

# Step 2: Load the Excel file
df = pd.read_excel(file_path, sheet_name=0)

# Step 3: Ask for Projected Numbers
projected_numbers_input = input("Enter Projected Numbers (default is 80.08): ")
projected_numbers = float(projected_numbers_input) if projected_numbers_input else 80.08

df = df.drop(labels=[0,1,2,3,4,5,6,7,8,9,324,325], axis=0)
df = df.drop(labels=['Unnamed: 1','Unnamed: 3','Unnamed: 4','Unnamed: 5','Unnamed: 6','Unnamed: 7','Unnamed: 8','Unnamed: 9','Unnamed: 10','Unnamed: 11','Unnamed: 12','Unnamed: 13','Unnamed: 14','Unnamed: 15','Unnamed: 19','Unnamed: 18','Unnamed: 21','Unnamed: 22','Unnamed: 24','Unnamed: 20'], axis=1)
df.rename(columns={"Unnamed: 0": "WRIN", "Unnamed: 2": "Description", "Unnamed: 16": "Usage Last 7 Days","Unnamed: 17": "POS Usg. per 1000 Saleslast 4 Weeks", "Unnamed: 23" : "Usage Last Month"}, inplace=True)

# Adding the new column
df['Last 7 Days * Projection'] = df['Usage Last 7 Days'] * projected_numbers
df['POS Usg. per 1000 Saleslast 4 Weeks * Projection'] = df['POS Usg. per 1000 Saleslast 4 Weeks'] * projected_numbers
df['Usage Last Month * Projection'] = df['Usage Last Month'] * projected_numbers

df['Max Value'] = df[['Last 7 Days * Projection', 
                      'POS Usg. per 1000 Saleslast 4 Weeks * Projection', 
                      'Usage Last Month * Projection']].apply(lambda row: row.max(), axis=1)

# Define a function to highlight a specific column
def highlight_max_value(column):
    # Apply style to the whole column
    return ['background-color: yellow'] * len(column)

# Apply the highlighting function to the DataFrame
df = df.style.apply(lambda x: highlight_max_value(x) if x.name == 'Max Value' else [''] * len(x), axis=0)

# Save the modified file in .xlsx format
new_file_name = 'Modified_' + os.path.splitext(file_name)[0] + '.xlsx'
new_file_path = os.path.join(os.path.expanduser('~'), 'Downloads', new_file_name)
df.to_excel(new_file_path, index=False)

print(f"The file has been modified and saved as {new_file_path}")