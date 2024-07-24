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


