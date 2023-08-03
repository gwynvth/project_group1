import csv
from pathlib import Path

# create a file to csv file. 
fp = Path.cwd()/"csv_reports"/"Overheads.csv"

# read the csv file to append profit and quantity  from the csv.
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) # skip header

    # create an empty lists to store time sheet and sales record
    Overheads=[] 

    # append time sheet and sales record into the salesRecords list
    for row in reader:
        #get the employee id, toal hours, break hours, and sales for each record
        #and append the salesRecords list
        Overheads.append([row[0],row[1]])  

#print(Overheads)



Highest_expense_name = None 
Highest_expense_amount = 0.0 
 
# Loop through the data to find the highest overhead expense 
for item in Overheads: 
    expense_name = item[0] 
    expense_amount = float(item[1]) 
     
    if expense_amount > Highest_expense_amount: 
        Highest_expense_amount = expense_amount 
        Highest_expense_name = expense_name 
 
print(f"[HIGHEST OVERHEAD]: {Highest_expense_name.upper()} : {Highest_expense_amount}%")




