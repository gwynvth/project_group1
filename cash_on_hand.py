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


def compute_difference(cashonhand):
    highest_increment = 0
    highest_increment_day = None
    differences = []

    for item in range(1,len(cashonhand)):
        day, COH = int(cashonhand[item][0]), int(cashonhand[item][1])
        prev_COH = int(cashonhand[item - 1][1])

        difference = COH - prev_COH
        differences.append((day, difference))

        if difference > highest_increment:
            highest_increment = difference
            highest_increment_day = day
        
    return differences, highest_increment_day, highest_increment

differences, highest_increment_day, highest_increment = compute_difference(cashonhand)

print("Differences in COH between consecutive days:")
for day, difference in differences:
    if difference < 0:
        print(f"[CASH DEFICIT] Day: {day}, AMOUNT: USD{abs(difference)}")
    elif difference > 0:
        print(f"[CASH SURPLUS] Day: {day}, AMOUNT: USD{difference}")

print(f"\nDay with the highest increment: Day {highest_increment_day}, Increment: {highest_increment}")














  













