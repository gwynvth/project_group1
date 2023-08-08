import csv
from pathlib import Path

# create a file to csv file. 
fp = Path.cwd()/"csv_reports"/"Overheads.csv"

# read the csv file to find the highest overhead category from the csv.
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) # skip header

    # create an empty lists to store the expenses
    overheads=[] 

    # append expenses and their respective percentage into the Overheads list
    for row in reader:
        #get the percentage for each expenses
        #and append the Overheads list
        overheads.append([row[0],row[1]])  

#print(overheads)

# def overheads(overhead_data):
#     highest_expense_name = None
#     highest_expense_amount = 0

#     # Loop through the data to find the highest overhead expense
#     for item in overhead_data:
#         expense_name = item[0]
#         expense_amount = float(item[1])

#         if expense_amount > highest_expense_amount:
#             highest_expense_amount = expense_amount
#             highest_expense_name = expense_name

#     highest_overheads = (highest_expense_amount / total_overheads) * 100 if total_overheads > 0 else 0

#     return f"[HIGHEST OVERHEAD] {highest_expense_name.upper()}: {highest_overheads:.2f}%"

# # Calculate the total overheads
# total_overheads = sum(float(item[1]) for item in ooverheads)

# # Call the function and print the result
# highest_overhead_info = overheads(ooverheads)
# print(highest_overhead_info)

def overheads_function():
    highest_expense_name = None
    highest_expense_amount = 0

    # Calculate the total overheads
    total_overheads = sum(float(item[1]) for item in overheads)

    # Loop through the data to find the highest overhead expense
    for item in overheads:
        expense_name = item[0]
        expense_amount = float(item[1])

        if expense_amount > highest_expense_amount:
            highest_expense_amount = expense_amount
            highest_expense_name = expense_name

    highest_overheads = (highest_expense_amount / total_overheads) * 100 if total_overheads > 0 else 0

    return f"[HIGHEST OVERHEAD] {highest_expense_name.upper()}: {highest_overheads:.2f}%"

# Call the function and print the result
highest_overhead_info = overheads_function()
print(highest_overhead_info)






