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

# method 1) def cash_on_hand_data(cashonhand):
#     highestincrement=0
#     difference=[]

#     for item in range(1,len(cashonhand)):
#         diff=cashonhand[item] - cashonhand[item-1]
#         difference.append(diff)

#         if diff > highestincrement:
#             highestincrement=diff
#             highestincrementday=item
#     return difference, highestincrementday, highestincrement


#method 2
#max_increment = 0
#max_increment_day = None
#max_increment_amount = None

 #Initialize variables for calculating the difference in Cash-on-Hand
#previous_cash_on_hand = None
#total_cash_difference = 0
#cash_on_hand = row[1]

# Loop through the data
#for day in cashonhand:
#    if previous_cash_on_hand is not None:
#        difference = previous_cash_on_hand - cash_on_hand
#        total_cash_difference += difference
#        if difference > max_increment:
#            max_increment = difference
#            max_increment_day = day
#            max_increment_amount = previous_cash_on_hand

#    previous_cash_on_hand = cash_on_hand

# Calculate the final Cash-on-Hand
#final_cash_on_hand = int(previous_cash_on_hand + total_cash_difference)

# Output the results
#print(f"Difference in Cash-on-Hand: {int(total_cash_difference)}")
#print(f"Final Cash-on-Hand: {final_cash_on_hand}")
#print(f"Day of the highest increment: {max_increment_day}")
#print(f"Amount of the highest increment: {int(max_increment_amount)}")



#method 3
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
        print(f"Day {day}: {abs(difference)}")
    elif difference > 0:
        print(f"Day {day}: {difference}")

print(f"\nDay with the highest increment: Day {highest_increment_day}, Increment: {highest_increment}")

#method4 
# create an empty lists to store cash on hand difference 
#cashonhand=[]  
#nextcashonhand =[] 
 
    # append day and cash on hand into the cash on hand difference list 

#for row in cashonhand: 
#        cash = int(row[1]) 
         
#        index = cashonhand.index(row) 
 
#        previous_day = int(cashonhand[index - 1][1]) 
#        if cash < previous_day: 
#            difference = previous_day - cash 
         
#        elif cash > previous_day: 
#            difference = cash - previous_day 
         
#        else: 
#            print("DAY1") 
 
#        nextcashonhand.append(difference) 
 
#nextcashonhand.pop(0) 
#print(nextcashonhand)













  













