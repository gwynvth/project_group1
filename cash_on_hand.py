from pathlib import Path
import csv

# create a file to csv file.
fp = Path.cwd()/"Cash_On_Hand.csv"

# read the csv file to append profit and quantity from the csv.
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) # skip header

    # create an empty lists to store time sheet and sales record
    cashonhand=[] 

    # append time sheet and sales record into the salesRecords list
    for row in reader:
        #get the day and cash on hand for each day
        cashonhand.append([row[0],row[1]])  
print(cashonhand) 
















