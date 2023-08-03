import csv
from pathlib import Path

# create a file to csv file. 
fp = Path.cwd()/"csv_reports"/"Cash_On_Hand.csv"

# read the csv file to append profit and quantity from the csv.
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) # skip header

    # create an empty lists to store time sheet and sales record
    cashonhand=[] 

    # append time sheet and sales record into the salesRecords list
    for row in reader:
        #get the employee id, toal hours, break hours, and sales for each record
        #and append the salesRecords list
        cashonhand.append([row[0],row[1]])   

print(cashonhand)

def cash_on_hand_data(cashonhand):
    highestincrement=0
    difference=[]

    for item in range(1,len(cashonhand)):
        diff=cashonhand[item] - cashonhand[item-1]
        difference.append(diff)

        if diff > highestincrement:
            highestincrement=diff
            highestincrementday=item
    return difference, highestincrementday, highestincrement




  













