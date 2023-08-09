import csv
from pathlib import Path

# create a file to csv file. 
fp = Path.cwd()/"csv_reports"/"Cash_On_Hand.csv"

# read the csv file to append from the csv.
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) # skip header

    # Create an empty list to store day and cash on hand
    cashonhand=[] 

    # Append cash into the cashonhand list
    for row in reader:
        # Get the day and cash 
        # and append the cashonhand list
        cashonhand.append([row[0],row[1]])   

# Create a function to calculate difference in cash on hand between consecutive days
def cash_on_hand():
    """
    - This function will return cash defitcit for specific days

    - Required parameter(s): none
    """
    # Create a list to store data
    differences = []

    # Calculate differences between consecutive days' cash amounts
    for item in range(1, len(cashonhand)):
        day, COH = int(cashonhand[item][0]), int(cashonhand[item][1])
        prev_COH = int(cashonhand[item - 1][1])

        difference = COH - prev_COH
        differences.append((day, difference))

    # Create a list to store data
    cash_deficit_strings = []
    # Iterate through the differences to identify cash deficit, if have
    for day, difference in differences:
        if difference < 0:
            # Create formatted strings for cash deficit occurrences and append to cash_deficit_strings
            cash_deficit_strings.append(f"[CASH DEFICIT] Day: {day}, AMOUNT: USD{abs(difference)}")

    # Join cash deficit strings with newline separator
    return '\n'.join(cash_deficit_strings)

# Calculate cash deficits using the cash_on_hand function
cash_on_hand_result = cash_on_hand()

#print the output
print(cash_on_hand_result)







  













