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

# def cash_on_hand_data(cashonhand):
#     highestincrement=0
#     difference=[]

#     for item in range(1,len(cashonhand)):
#         diff=cashonhand[item] - cashonhand[item-1]
#         difference.append(diff)

#         if diff > highestincrement:
#             highestincrement=diff
#             highestincrementday=item
#     return difference, highestincrementday, highestincrement

max_increment = 0
max_increment_day = None
max_increment_amount = None

# Initialize variables for calculating the difference in Cash-on-Hand
previous_cash_on_hand = None
total_cash_difference = 0
cash_on_hand = row[1]

# Loop through the data
for day, cash_on_hand in cashonhand:
    if previous_cash_on_hand is not None:
        difference = previous_cash_on_hand - cash_on_hand
        total_cash_difference += difference
        if difference > max_increment:
            max_increment = difference
            max_increment_day = day
            max_increment_amount = previous_cash_on_hand

    previous_cash_on_hand = cash_on_hand

# Calculate the final Cash-on-Hand
final_cash_on_hand = previous_cash_on_hand + total_cash_difference

# Output the results
print(f"Difference in Cash-on-Hand: {total_cash_difference}")
print(f"Final Cash-on-Hand: {final_cash_on_hand}")
print(f"Day of the highest increment: {max_increment_day}")
print(f"Amount of the highest increment: {max_increment_amount}")










  













