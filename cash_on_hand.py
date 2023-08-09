import csv
from pathlib import Path

# create a file to csv file. 
fp = Path.cwd()/"csv_reports"/"Cash_On_Hand.csv"

# read the csv file to append from the csv.
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) # skip header

    # create an empty list to store day and cash on hand
    cashonhand=[] 

    # append cash into the cashonhand list
    for row in reader:
        #get the day and cash 
        #and append the cashonhand list
        cashonhand.append([row[0],row[1]])   

#create a function to calculate difference in cash on hand between consecutive days
def cash_on_hand():
    """
    - this function will return cash defitcit for specific days
    - required parameters: none
    """
    highest_increment = 0
    highest_increment_day = None
    differences = []

    for item in range(1, len(cashonhand)):
        day, COH = int(cashonhand[item][0]), int(cashonhand[item][1])
        prev_COH = int(cashonhand[item - 1][1])

        difference = COH - prev_COH
        differences.append((day, difference))

        if difference > highest_increment:
            highest_increment = difference
            highest_increment_day = day

    # calculate cash defitcits 
    cash_deficit_strings = []
    for day, difference in differences:
        if difference < 0:
            cash_deficit_strings.append(f"[CASH DEFICIT] Day: {day}, AMOUNT: USD{abs(difference)}")
    
    return '\n'.join(cash_deficit_strings)

cash_on_hand_result = cash_on_hand()

#print the output
print(cash_on_hand_result)







  













